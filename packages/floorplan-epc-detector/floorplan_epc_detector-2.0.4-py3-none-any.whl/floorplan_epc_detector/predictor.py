import os
import logging
import numpy as np
from PIL import Image
from typing import List, Dict, Tuple, Optional
from floorplan_epc_detector.samclip.sam.model import OnnxSAM
from floorplan_epc_detector.samclip.clip.model import OnnxLip, softmax, get_probabilities

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FloorplanPredictor:
    def __init__(self, batch_size: int = 16):
        """Initialize the FloorplanPredictor with CLIP model.
        
        Args:
            batch_size: Batch size for processing multiple images at once
        """
        self.batch_size = batch_size
        self.model = OnnxLip(batch_size=batch_size, type='clip')
        self.categories = [
            "a photograph of a residential property interior",
            "a photograph of a property exterior featuring garden or street view",
            "an architectural floor plan",
            "an Energy Performance Certificate document",
            "a website icon or logo",
            "an emoji or emoticon",
            "a UI button or graphic",
        ]
        self.categories_map = {"a photograph of a residential property interior": "interior_photo",
                               "a photograph of a property exterior featuring garden or street view": "exterior_photo",
                               "an architectural floor plan": "floorplan",
                               "an Energy Performance Certificate document": "epc",
                               "a website icon or logo": "unrelated_image",
                               "an emoji or emoticon": "unrelated_image",
                               "a UI button or graphic": "unrelated_image"}
    
    def predict_batch(self, image_paths: List[str]) -> List[Tuple[str, float]]:
        try:
            # Load and convert images
            images = [Image.open(path).convert("RGB") for path in image_paths]
            
            # Prepare text categories for all images
            texts = {
                "classification": self.categories
            }
            
            # Get predictions from CLIP model
            _, logits = self.model.inference(images, texts)
            probs = logits['classification']
            probs = softmax(probs)
            
            # Process results
            results = []
            for prob in probs:
                category_idx = int(np.argmax(prob))
                confidence = float(prob[category_idx])
                results.append((self.categories_map[self.categories[category_idx]], confidence))
            
            return results
            
        except Exception as e:
            logger.error(f"Failed during batch prediction: {str(e)}")
            raise
    def get_raw_probabilities(self, image_path: str) -> Dict[str, float]:
        """
        Get raw probabilities for each category for a single image.
        
        Args:
            image_path: Path to the image file
        Returns:
            Dictionary mapping category names to their probabilities
        """
        try:
            # Load and convert image
            image = Image.open(image_path).convert("RGB")
            
            # Prepare text categories
            texts = {
                "classification": self.categories
            }
            
            # Get predictions from CLIP model
            _, logits = self.model.inference([image], texts)
            probs = logits['classification']
            probs = softmax(probs)[0]  # Get probabilities for the single image
            
            # Map categories to their probabilities
            prob_dict = {self.categories[i]: float(probs[i]) for i in range(len(self.categories))}
            for i in self.categories_map:
                if i in prob_dict:
                    prob_dict[self.categories_map[i]] = prob_dict.get(self.categories_map[i], 0) + prob_dict[i]
            final_dict = {k: v for k, v in prob_dict.items() if k in self.categories_map.values()}
            return final_dict
            
        except Exception as e:
            logger.error(f"Failed to get raw probabilities: {str(e)}")
            raise

    def predict_with_confidence(self, image_path: str, confidence_threshold) -> Tuple[str, float]:
        """
        Predict the category for a single image.
        
        Args:
            image_path: Path to the image file
            
        Returns:
            Tuple containing (predicted_category, confidence)
        """
        results = self.predict_batch([image_path])
        return results[0]