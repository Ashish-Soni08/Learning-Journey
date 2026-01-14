# Describe-and-Generate Game 🖍️

This application is an interactive "Describe-and-Generate" game that leverages advanced AI models to generate creative images based on the captions derived from an initial uploaded image.

## How It Works
1. **Image Captioning**: The app uses the `salesforce/blip-image-captioning-base` model to generate a descriptive caption from the uploaded image.
2. **Image Generation**: The app then feeds this caption into the `runwayml/stable-diffusion-v1-5` model, which generates a new image based on the caption.

## Features
- **Upload an Image**: Start by uploading an image of your choice.
- **Caption Generation**: The app will automatically generate a caption describing the uploaded image.
- **Image Generation**: Based on the generated caption, the app will create a new, AI-generated image.
- **Interactive Interface**: Built using Gradio, the interface is simple and user-friendly, allowing you to experiment with different images and see the AI's creative output.

## Models Used
- **Captioning Model**: `salesforce/blip-image-captioning-base`
- **Image Generation Model**: `runwayml/stable-diffusion-v1-5`

## Software Packages
- **Gradio**: Used to create the interactive web interface.
- **Transformers**: Used for the image captioning model.
- **Diffusers**: Used for the image generation model.
- **Spaces**: Utilized for GPU acceleration during model execution.

## How to Use
1. **Upload an Image**: Use the "Your first image" button to upload any image.
2. **Generate**: Click the "Caption and generate" button.
3. **View Results**: The app will display the generated caption and the new image created based on that caption.

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