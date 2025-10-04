import scipy
import errno
from numpy import linalg as LA
import os
import logging
from pathlib import Path
from typing import List, Tuple, Union, Iterable, Iterator, TypeVar, Optional
import gdown

import numpy as np
import onnxruntime as ort
from PIL import Image

from floorplan_epc_detector.samclip.utils import ensemble_prompt
from floorplan_epc_detector.samclip.clip import Preprocessor, Tokenizer
from floorplan_epc_detector.samclip.clip.siglip_tokenizer import SiglipTokenizer
from floorplan_epc_detector.samclip.clip.siglip_image_processor import image_transform

logging.basicConfig(level=logging.INFO)
T = TypeVar("T")

def softmax(x: np.ndarray) -> np.ndarray:
    """
    Computes softmax values for each sets of scores in x.
    This ensures the output sums to 1 for each image (along axis 1).
    """

    # Exponents
    exp_arr = np.exp(x)

    return exp_arr / np.sum(exp_arr, axis=1, keepdims=True)


def cosine_similarity(
    embeddings_1: np.ndarray, embeddings_2: np.ndarray
) -> np.ndarray:
    """Compute the pairwise cosine similarities between two embedding arrays.

    Args:
        embeddings_1: An array of embeddings of shape (N, D).
        embeddings_2: An array of embeddings of shape (M, D).

    Returns:
        An array of shape (N, M) with the pairwise cosine similarities.
    """

    if len(embeddings_1.shape) != 2 or len(embeddings_2.shape) != 2:
        raise ValueError(
            f"Expected 2-D arrays but got shapes {embeddings_1.shape} and {embeddings_2.shape}."
        )

    d1 = embeddings_1.shape[1]
    d2 = embeddings_2.shape[1]

  

    if d1 != d2:
        raise ValueError(
            "Expected second dimension of embeddings_1 and embeddings_2 to "
            f"match, but got {d1} and {d2} respectively."
        )


    def normalize(embeddings):
        return embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)

    embeddings_1 = normalize(embeddings_1)
    embeddings_2 = normalize(embeddings_2)

    return embeddings_1 @ embeddings_2.T


def get_probabilities(image_embedding: list,
                           queries: dict):
    """Compute pairwise similarity scores between two arrays of embeddings.

    args: image_embedding: list of images
    queries: dictionary of pre-computed text embeddings
    """

    res_dict = {}
    logits_dict = {}

    for key, query in queries.items():
      if not isinstance(query, (np.ndarray, np.generic) ):
        continue

      if image_embedding.ndim == 1:
          # Convert to 2-D array using x[np.newaxis, :]
          # and remove the extra dimension at the end.
          res_dict[key] = softmax(get_probabilities(
              image_embedding[np.newaxis, :], query
          )[0])

      if query.ndim == 1:
          # Convert to 2-D array using x[np.newaxis, :]
          # and remove the extra dimension at the end.
          res_dict[key] = softmax(get_probabilities(
              image_embedding, query[np.newaxis, :]
          )[:, 0])

      logits_dict[key] = cosine_similarity(image_embedding, query) * 100
      res_dict[key] = softmax(logits_dict[key])[0]


    return res_dict, logits_dict


class OnnxLip:
    """
    This class can be utilised to predict the most relevant text snippet, given
    an image, without directly optimizing for the task, similarly to the
    zero-shot capabilities of GPT-2 and 3. The difference between this class
    and [CLIP](https://github.com/openai/CLIP) is that here we don't depend on
    `torch` or `torchvision`.
    """


    def __init__(
        self, model: str = "ViT-B/32", 
        batch_size: Optional[int] = None, 
        type='siglip',
        size=384,
        device='cuda',
        trt=False
    ):
        """
        Instantiates the model and required encoding classes.

        Args:
            model: The model to utilise. Currently ViT-B/32 
            batch_size: If set, splits the lists in `get_image_embeddings`
                and `get_text_embeddings` into batches of this size before
                passing them to the model. The embeddings are then concatenated
                back together before being returned. This is necessary when
                passing large amounts of data (perhaps ~100 or more).
            
        """ 
        assert device in ['cpu', 'cuda'], 'please use either cuda or cpu!'

        self.providers = [
                    'CPUExecutionProvider'
                ]

        if device == 'cuda':
            self.providers.insert(0, 'CUDAExecutionProvider')

        if trt:
            self.providers.insert(0, 'TensorrtExecutionProvider')
     

        if self.providers:
            logging.info(
                "Available providers for ONNXRuntime: %s", ", ".join(self.providers)
            )
 

        self.embedding_size = 512

        assert type in ['siglip', 'clip', 'surgery', 'siglip_full'], 'please choose either: siglip, siglip_full, clip, or surgery'
        self.type = type

        self._model_urls = {
            'clip_image_model_vitb32.onnx': 'https://drive.google.com/uc?id=1WbRBDaBLsVdAZRD_1deq0uYGhIVFNoAi',
            'clip_text_model_vitb32.onnx': 'https://drive.google.com/uc?id=1EC2ju-gIlLfBJ3un-1G5QFQzYi8DoA9o',
            'clip_image_model_surgery_vitb32.onnx': 'https://drive.google.com/uc?id=1loyhPLYciY5eCU2Iw5kllNOw1w-PwRO0',
            'clip_text_model_surgery_vitb32.onnx': 'https://drive.google.com/uc?id=1RBfUlwcvKZJPYzRWEOtATuEfsSOw33Vj',
            'siglip_image_384_fp16.onnx': 'https://drive.google.com/uc?id=1vZvBZIDPzax2AfoYwRWO7neo2SxoScEX',
            'siglip_text_384_fp16.onnx': 'https://drive.google.com/uc?id=1oUl6H3Y0Az8F1GGXVmEPPcy52dasWeiD',
            'siglip_full_384_fp16.onnx': 'https://drive.google.com/uc?id=1iGrC4goUs8RdR_lF9SrpQl81pgang-di',
            'bpe_simple_vocab_16e6.txt.gz': 'https://drive.google.com/uc?id=1zPQqH85z5zS8zBSKXI6VqpR9JdG8hz5s'
        }

        self.image_model, self.text_model = self._load_models(model)


        if 'siglip' in type:
            #currently only supporting 384
            assert size in [384, 224], 'please choose either a 384, or 224 input size for SigLIP!'

            try:
                tokenizer_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', f'siglip-base-patch16-{size}')
                os.makedirs(tokenizer_dir, exist_ok=True)
                tokenizer_path = os.path.join(tokenizer_dir, 'spiece.model')

                if not os.path.exists(tokenizer_path):
                    logging.info(f"Tokenizer file not found at {tokenizer_path}, downloading...")
                    tokenizer_url = "https://drive.google.com/uc?id=1FGhJS6mzMzd_tN1rwCZZ5OQrEWETqGBg"
                    success = gdown.download(url=tokenizer_url, output=tokenizer_path, fuzzy=True)
                    
                    if not success:
                        raise RuntimeError(f"Failed to download tokenizer file to {tokenizer_path}")
                    
                    if not os.path.exists(tokenizer_path):
                        raise RuntimeError(f"Tokenizer file not found after download: {tokenizer_path}")
                    
                    if os.path.getsize(tokenizer_path) == 0:
                        os.remove(tokenizer_path)
                        raise RuntimeError(f"Downloaded tokenizer file is empty: {tokenizer_path}")
                    
                    logging.info(f"Tokenizer downloaded successfully to {tokenizer_path}")
                    logging.info(f"File size: {os.path.getsize(tokenizer_path)} bytes")

                self._siglip_tokenizer = SiglipTokenizer(
                    vocab_file=tokenizer_path,
                    model_input_names=["input_ids"]
                )
            except Exception as e:
                logging.error(f"Error setting up tokenizer: {str(e)}")
                logging.error(f"Tokenizer path: {tokenizer_path}")
                logging.error(f"Directory exists: {os.path.exists(tokenizer_dir)}")
                if os.path.exists(tokenizer_dir):
                    logging.error(f"Directory permissions: {oct(os.stat(tokenizer_dir).st_mode)[-3:]}")
                raise RuntimeError(f"Failed to setup tokenizer: {str(e)}") from e
            
            self._siglip_preprocessor = image_transform(image_size=size, is_train=False)
        else:
            self._tokenizer = Tokenizer(device=device)
            self._preprocessor = Preprocessor(type=type)

        self._batch_size = batch_size

    @property
    def EMBEDDING_SIZE(self):
        raise RuntimeError("OnnxModel.EMBEDDING_SIZE is no longer supported,f please use the instance attribute: onnx_model.embedding_size")


    def _load_models(
        self,
        model: str,
    ) -> Tuple[ort.InferenceSession, ort.InferenceSession]:
      
        if self.type == 'surgery':
            IMAGE_MODEL_FILE = "clip_image_model_surgery_vitb32.onnx"
            TEXT_MODEL_FILE = "clip_text_model_surgery_vitb32.onnx"
        elif self.type == 'siglip':
            IMAGE_MODEL_FILE = "siglip_image_384_fp16.onnx"
            TEXT_MODEL_FILE = "siglip_text_384_fp16.onnx"

        elif self.type == 'siglip_full':
            IMAGE_MODEL_FILE = "siglip_full_384_fp16.onnx"
            TEXT_MODEL_FILE = "+"

        else:
            IMAGE_MODEL_FILE = "clip_image_model_vitb32.onnx"
            TEXT_MODEL_FILE = "clip_text_model_vitb32.onnx"


        base_dir = os.path.dirname(os.path.abspath(__file__))

        models = []

        for model_file in [IMAGE_MODEL_FILE, TEXT_MODEL_FILE]:
            path = os.path.join(base_dir, "data", model_file)
            if model_file == "+":
               return models[0], model_file
            models.append(self._load_model(path))

        return models[0], models[1]

    def _load_model(self, path: str):
        """Load or download the model file.
        
        Args:
            path: Path where the model should be loaded from or downloaded to.
            
        Returns:
            ort.InferenceSession: The loaded model.
            
        Raises:
            RuntimeError: If model cannot be loaded or downloaded.
        """
        try:
            # Get directory and filename
            data_dir = os.path.dirname(path)
            filename = os.path.basename(path)

            # Check if we have a download URL for this model
            if filename not in self._model_urls:
                raise ValueError(f"No download URL found for model {filename}")

            # Create all parent directories
            logging.info(f"Creating directory: {data_dir}")
            os.makedirs(data_dir, exist_ok=True)

            if os.path.exists(path):
                logging.info(f"Loading existing model from {path}")
                try:
                    return ort.InferenceSession(path, providers=self.providers)
                except Exception as e:
                    logging.warning(f"Failed to load existing model, will try to download again: {str(e)}")
                    if os.path.exists(path):
                        os.remove(path)

            # Download the model file
            logging.info(f"Downloading model to {path}")
            logging.info(f"Download URL: {self._model_urls[filename]}")
            
            success = gdown.download(
                url=self._model_urls[filename],
                output=path,
                fuzzy=True,
                quiet=False
            )

            if not success:
                raise RuntimeError(f"gdown.download returned False for {path}")

            if not os.path.exists(path):
                raise RuntimeError(f"Model file not found at {path} after download")

            if os.path.getsize(path) == 0:
                os.remove(path)
                raise RuntimeError(f"Downloaded file is empty: {path}")

            logging.info(f"Model downloaded successfully to {path}")
            logging.info(f"File size: {os.path.getsize(path)} bytes")
            
            return ort.InferenceSession(path, providers=self.providers)

        except Exception as e:
            logging.error(f"Error loading/downloading model: {str(e)}")
            logging.error(f"Model path: {path}")
            logging.error(f"Current working directory: {os.getcwd()}")
            logging.error(f"Directory exists: {os.path.exists(os.path.dirname(path))}")
            logging.error(f"Directory permissions: {oct(os.stat(os.path.dirname(data_dir)).st_mode)[-3:]}")
            raise RuntimeError(f"Failed to load or download model: {str(e)}") from e

    def get_image_embeddings(
        self,
        images: Iterable[Union[Image.Image, np.ndarray]],
        with_batching: bool = True,
    ) -> np.ndarray:
        """Compute the embeddings for a list of images.

        Args:
            images: A list of images to run on. Each image must be a 3-channel
                (RGB) image. Can be any size, as the preprocessing step will
                resize each image to size (224, 224).
            with_batching: Whether to use batching - see the `batch_size` param
                in `__init__()`

        Returns:
            An array of embeddings of shape (len(images), embedding_size).
        """
        if not with_batching or self._batch_size is None:
            # Preprocess images
            if 'siglip' in self.type:
                images = [
                    np.expand_dims(self._siglip_preprocessor(image).numpy(), 0) for image in images
                ]
            else:
                images = [
                    self._preprocessor.encode_image(image) for image in images
                ]


            
            if not images:
                return self._get_empty_embedding()

            batch = np.concatenate(images)

            if self.type == 'siglip':
                incoming = {"pixel_values": batch}

                hidden, pooled = self.image_model.run(None, incoming)
                self.hidden_image = hidden
                
                return pooled
            else:
                incoming = {"IMAGE": batch}
                return self.image_model.run(None, incoming)[0]

        else:
            embeddings = []
            for batch in to_batches(images, self._batch_size):
                embeddings.append(
                    self.get_image_embeddings(batch, with_batching=False)
                )

            if not embeddings:
                return self._get_empty_embedding()

            return np.concatenate(embeddings)

    def get_text_embeddings(
        self, texts: Iterable[str], with_batching: bool = True
    ) -> np.ndarray:
        """Compute the embeddings for a list of texts.

        Args:
            texts: A list of texts to run on. Each entry can be at most
                77 characters.
            with_batching: Whether to use batching - see the `batch_size` param
                in `__init__()`

        Returns:
            An array of embeddings of shape (len(texts), embedding_size).
        """
        if not with_batching or self._batch_size is None:
           
          
            if self.type == 'siglip':

                text = self._siglip_tokenizer(texts, 
                        return_tensors='np', 
                        padding="max_length",
                        truncation=True
                        )
                if len(text) == 0:
                    return self._get_empty_embedding()

                #text is already in a input_ids keypair here 
                hidden, pooled = self.text_model.run(None, {'input_ids': text['input_ids'].astype(np.int64)})
                
                #needs adjusting to a list followed by np.concatenate
                self.hidden_text =  hidden

                return pooled

            else:

                text = self._tokenizer.encode_text(texts)
                if len(text) == 0:
                    return self._get_empty_embedding()
    
                incoming = {"TEXT": text}
                return self.text_model.run(None, incoming)[0]

            
        else:
            embeddings = []
         
            for batch in to_batches(texts, self._batch_size):
                embeddings.append(
                    self.get_text_embeddings(batch, with_batching=False)
                )
   
            if not embeddings:
                return self._get_empty_embedding()

            return np.concatenate(embeddings)

    def _get_empty_embedding(self):
        return np.empty((0, self.embedding_size), dtype=np.float32)
    
    def inference(self, images, texts):

        """
        This could use separation into three models for efficiency
        ie one time image embedding, multiple text contexts pre-computed
        and final inference afterwards instead of recomputing image embedding multiple time
        """

        probs = {}
        contexts = {}
        logits = {}

        if self.type == 'siglip_full':

            """

      
          
            """

            #outputting only image logits right now
            #images = self._preprocessor.encode_image(images[0])

            ####image processing needs changing to open clip version
            images = [self._siglip_preprocessor(i).numpy() for i in images]

            for k,v in texts.items():

                for k,v in texts.items():
                    incoming_texts = self._siglip_tokenizer(
                            text=texts[k], 
                            padding="max_length", 
                            return_tensors="np",
                            truncation=True
                            )['input_ids']

                
                    res = self.image_model.run(None, {'input_ids': incoming_texts,'pixel_values': images})[0]
  

                    logits[k] = res[0]
                    probs[k] = scipy.special.expit(logits[k])
               
        
        else:
            
            image_embeddings = self.get_image_embeddings(images)
            for k,v in texts.items():
                contexts[k] =  self.get_text_embeddings(texts[k])

          
            probs, logits = get_probabilities(image_embeddings, contexts)

        
        return probs, logits
            
     
        
            


def to_batches(items: Iterable[T], size: int) -> Iterator[List[T]]:
    """
    Splits an iterable (e.g. a list) into batches of length `size`. Includes
    the last, potentially shorter batch.

    Examples:
        >>> list(to_batches([1, 2, 3, 4], size=2))
        [[1, 2], [3, 4]]
        >>> list(to_batches([1, 2, 3, 4, 5], size=2))
        [[1, 2], [3, 4], [5]]

        # To limit the number of batches returned
        # (avoids reading the rest of `items`):
        >>> import itertools
        >>> list(itertools.islice(to_batches([1, 2, 3, 4, 5], size=2), 1))
        [[1, 2]]

    Args:
        items: The iterable to split.
        size: How many elements per batch.
    """
    if size < 1:
        raise ValueError("Chunk size must be positive.")

    batch = []
    for item in items:
        batch.append(item)

        if len(batch) == size:
            yield batch
            batch = []

    # The last, potentially incomplete batch
    if batch:
        yield batch



            




