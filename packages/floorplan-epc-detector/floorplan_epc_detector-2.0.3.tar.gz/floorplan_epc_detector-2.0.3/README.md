# EPC Floorplan Image Detection

[![Run In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/163GdAsuENBTDnlpefZUhDlVqwi70z8En?usp=sharing)

[![Colab Badge](https://img.shields.io/badge/Colab-Train%20Now-yellow?logo=googlecolab)](https://colab.research.google.com/drive/1oaEwwFl8gZB3vSTMySn2dmUIRP5S6yFU?usp=drive_link)

A Python package for classifying images as EPCs, floorplans, property photos, or exterior shots using SAM-CLIP, a state-of-the-art vision model that combines Segment Anything Model (SAM) with Contrastive Language-Image Pre-Training (CLIP).

## What's New in Version 2.0.0

Major update replacing the YOLO-based classifier with SAM-CLIP for improved accuracy and robustness:

- **SAM-CLIP Integration**: Leverages both semantic segmentation and visual-language understanding
- **Improved Accuracy**: Better handling of complex layouts and variations in image styles
- **More Robust**: Enhanced performance on edge cases and unusual image formats
- **Zero-shot Capabilities**: Potential for recognizing new image types without retraining

## Quick Start Guide

Get started with image classification in just a few steps:

1. **Install the package:**
   ```bash
   pip install floorplan-epc-detector==2.0.0
   ```

2. **Basic Usage:**
   ```python
   from floorplan_epc_detector import FloorplanPredictor

   # Initialize the predictor (models will be downloaded automatically)
   predictor = FloorplanPredictor()

   # Classify a single image
   prediction, confidence = predictor.predict_with_confidence(
       "path/to/your/image.jpg",
       confidence_threshold=0.7
   )
   print(f"Image Type: {prediction}")
   print(f"Confidence: {confidence:.2%}")
   ```

3. **Batch Processing Example:**
   ```python
   # Process multiple images
   images = [
       "image1.jpg",
       "image2.png",
       "floor_plan.jpeg"
   ]

   for image_path in images:
       # Get detailed probabilities
       probs = predictor.get_raw_probabilities(image_path)
       print(f"\nAnalyzing: {image_path}")
       print(f"Probabilities: {probs}")
       
       # Get final prediction
       prediction, confidence = predictor.predict_with_confidence(
           image_path,
           confidence_threshold=0.7
       )
       print(f"Predicted Type: {prediction}")
       print(f"Confidence: {confidence:.2%}")
   ```

4. **Understanding Results:**
   - The predictor classifies images into 4 categories:
     - `epc`: Energy Performance Certificate
     - `floorplan`: Floor Plans
     - `interior`: Interior Property Photos
     - `exterior`: Exterior Property Photos
   - Confidence scores range from 0 to 1 (shown as percentages)
   - The default confidence threshold is 0.7 (70%)

5. **Best Practices:**
   - Use clear, well-lit images
   - Ensure images are readable and not corrupted
   - Higher resolution images generally work better
   - Supported formats: JPG, JPEG, PNG
   - For batch processing, handle each image's results individually

## Prerequisites

- Python 3.7 or higher

## Installation

```bash
pip install floorplan-epc-detector==2.0.0
```

## Real-World Example

Here's a complete example showing how to process multiple images and handle results:

```python
import os
from floorplan_epc_detector import FloorplanPredictor

# Initialize predictor
predictor = FloorplanPredictor()

# List of images to process
test_images = [
    "property_photo.jpeg",
    "epc_certificate.png",
    "house_floorplan.jpg"
]

# Process each image
for image_name in test_images:
    if not os.path.exists(image_name):
        print(f"Image not found: {image_name}")
        continue
        
    print(f"\nAnalyzing image: {image_name}")
    
    try:
        # Get detailed classification probabilities
        raw_probabilities = predictor.get_raw_probabilities(image_name)
        print(f"Detailed probabilities:")
        for class_name, prob in raw_probabilities.items():
            print(f"  {class_name}: {prob:.2%}")
        
        # Get final prediction with confidence
        prediction, confidence = predictor.predict_with_confidence(
            image_name, 
            confidence_threshold=0.7
        )
        print(f"Final Result:")
        print(f"  Type: {prediction}")
        print(f"  Confidence: {confidence:.2%}")
        
    except Exception as e:
        print(f"Error processing {image_name}: {e}")
```

This example shows:
- How to handle multiple images
- Error handling for missing files
- Getting detailed classification probabilities
- Making final predictions with confidence scores
- Proper formatting of results

## Features

- Image Classification into 4 categories:
  - EPC (Energy Performance Certificate)
  - Floorplans
  - Property Interior Images
  - Property Exterior Images
- Confidence Scoring
- Automatic model download from private/public repositories
- Progress bar for model downloads
- Configurable confidence thresholds
- Raw probability access for advanced use cases

## Usage

```python
import os
from floorplan_epc_detector import FloorplanPredictor, FloorplanPredictorError

# --- Configuration for Private Repositories --- 
# If the model is hosted in a private GitHub repository, 
# you MUST provide a GitHub Personal Access Token (PAT).
# Set it as an environment variable:
# export GITHUB_TOKEN="your_github_pat_here"
# Ensure the token has the 'repo' scope to access private repository content.

github_token = os.environ.get("GITHUB_TOKEN")

try:
    # Initialize the predictor with options
    predictor = FloorplanPredictor(
        github_token=github_token,  # Optional: For private repos
        model_path="custom/path/model.onnx",  # Optional: Custom model path
        skip_download=False  # Optional: Skip auto-download
    )

    # Basic prediction (returns just the class)
    predicted_class = predictor.predict("path/to/your/image.jpg")
    print(f"Predicted Class: {predicted_class}")

    # Prediction with confidence score
    predicted_class, confidence = predictor.predict_with_confidence(
        "path/to/your/image.jpg",
        confidence_threshold=0.7  # Optional: Default is 0.7
    )
    print(f"Predicted Class: {predicted_class}")
    print(f"Confidence: {confidence:.2%}")

    # Get raw probabilities for all classes
    probabilities = predictor.get_raw_probabilities("path/to/your/image.jpg")
    print("Raw probabilities:", probabilities)

except FloorplanPredictorError as e:
    print(f"An error occurred: {e}")
    # Handle specific errors:
    # - ModelDownloadError
    # - ImageLoadError
    # - InferenceError
```

## Model Downloading

The package supports two ways to use the model:

1. **Automatic Download**: The model will be automatically downloaded from the configured repository on first use
2. **Local Model**: Provide a local path to an existing model file

- The package automatically attempts to download the `model.onnx` file using the GitHub API if it's not found locally
- Progress bar shows download progress for large model files
- Supports Git LFS for efficient model file handling
- **Private Repositories:** Downloading from private GitHub repositories requires a `GITHUB_TOKEN` environment variable or direct token provision

## Error Handling

The package provides specific error types for better error handling:

- `ModelDownloadError`: Issues with model downloading
- `ImageLoadError`: Problems with image loading or preprocessing
- `InferenceError`: Issues during model inference
- `FloorplanPredictorError`: Base class for all package errors

## Common Errors & Troubleshooting

*   **`ModelDownloadError: ... 404 Not Found ...`**: 
    *   Check if the `GITHUB_TOKEN` environment variable is set correctly (if accessing a private repo)
    *   Verify the token is valid, not expired, and has the **`repo` scope** enabled
    *   Confirm the repository and model path settings are correct

*   **`ModelDownloadError: ... 403 Forbidden ...`**: 
    *   Usually indicates the provided `GITHUB_TOKEN` lacks necessary permissions

*   **`FloorplanPredictorError: GITHUB_TOKEN is required...`**: 
    *   Set the `GITHUB_TOKEN` environment variable for private repository access

*   **`FileNotFoundError` or `ImageLoadError`**: 
    *   Ensure the image path is correct and the file exists
    *   Verify the image format is supported (JPEG, PNG, etc.)

*   **ONNX Runtime Issues**: 
    *   Ensure `onnxruntime` is installed correctly for your OS
    *   Check Python version compatibility

## Running Tests (Development)

1.  Clone the repository
2.  Install development dependencies: `pip install -r requirements.txt`
3.  Set the `GITHUB_TOKEN` environment variable if testing with private repo
4.  Place test images in the root directory
5.  Run the test script: `python test.py`

## Requirements

- Python >= 3.7
- onnxruntime >= 1.12.0
- onnxruntime-extensions
- numpy >= 1.19.0
- torch >= 2.0.0
- torchvision >= 0.15.0
- huggingface-hub
- sentencepiece
- opencv-python-headless
- ftfy
- regex
- scipy
- gdown
- Pillow >= 10.0.0
- tqdm >= 4.65.0

## License

MIT License

## Author

Oliver Brown
