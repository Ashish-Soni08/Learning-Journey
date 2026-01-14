# Bean Plant Health Predictor

This application is designed to help farmers quickly identify the health of bean plants by analyzing images of their leaves. The app uses a Vision Transformer (ViT) model to classify images into three categories: Angular Leaf Spot, Bean Rust, and Healthy. This tool can be deployed on a drone for real-time monitoring of crops, enabling timely treatment of diseased plants.

## Use Case

Farmers need to monitor the health of their bean plants regularly to prevent the spread of diseases. This app provides a machine learning-based solution to automate the identification of plant diseases, which can be particularly useful when integrated with drone technology.

## Features
- **Image Classification**: Upload an image of a bean leaf, and the app will classify it into one of the following categories:
  - Angular Leaf Spot
  - Bean Rust
  - Healthy

## Model Details
- **Model Used**: Vision Transformer (ViT) - base-sized model fine-tuned on the Beans dataset.
- **Image Processor**: The app uses the `ViTImageProcessor` for preparing images before classification.
- **Labels**: The possible outcomes are `angular_leaf_spot`, `bean_rust`, and `healthy`.

## How to Use
1. **Upload an Image**: Click on the image input field and upload a photo of a bean leaf.
2. **Get Results**: The app will classify the image and display the probabilities for each category.
3. **Interpret the Results**: The app shows the confidence levels for each label, helping farmers identify whether the plant is healthy or requires treatment.

## Technology Stack

- **Gradio**: Used to create the user interface.
- **PyTorch**: Utilized for running the model inference.
- **Hugging Face Transformers**: Provides the pre-trained Vision Transformer model.

## How to Install and Use the App Locally

### Prerequisites
- Python 3.8 or later
- `pip` package manager

#### Step 1: Clone the Repository
Clone the repository to your local machine using Git:

```bash
git clone <repository_url>
cd <repository_directory>
```

#### Step 2: Create a Virtual Environment

It is recommended to create a virtual environment to manage dependencies:

```bash
# Create a virtual environment
python -m venv venv

source venv/bin/activate
```

#### Step 3: Install Dependencies

Install the required Python packages using the requirements.txt file:

```bash
pip install -r requirements.txt
```

#### Step 4: Run the App

Once the dependencies are installed, you can start the app:

```bash
python app.py
```

The demo will open in a browser at `http://localhost:7860` if running from a file. If you are running within a notebook, the demo will appear embedded within the notebook.