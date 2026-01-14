# Stable Diffusion Image Generation App

This application allows you to generate images from text prompts using the Stable Diffusion model (`runwayml/stable-diffusion-v1-5`). With a simple interface powered by Gradio, you can input a prompt, adjust various parameters, and generate high-quality images.

## Features
- **Text-to-Image Generation**: Enter a text prompt, and the app will generate an image based on that prompt using the Stable Diffusion model.
- **Advanced Options**: Modify the image generation process with several customizable parameters:
  - **Negative Prompt**: Specify elements to exclude from the generated image.
  - **Inference Steps**: Adjust the number of steps used to denoise the image, affecting the image quality and detail.
  - **Guidance Scale**: Control how strongly the text prompt influences the final image.
  - **Image Dimensions**: Set the width and height of the generated image.

## How to Use
- **Enter a Prompt**: Type a description of the image you want to generate in the "Your prompt" textbox.
- **Adjust Advanced Options (optional)**:
  - Use the "Negative prompt" textbox to specify elements you do not want in the image.
  - Adjust the "Inference Steps" slider to change the number of denoising steps.
  - Adjust the "Guidance Scale" slider to control how closely the image follows the prompt.
  - Set the "Width" and "Height" sliders to determine the dimensions of the output image.
- **Generate the Image**: Click the "Submit" button to generate the image based on your settings.
- **View the Result**: The generated image will be displayed in the "Result" section.

## Technology Stack
- **Gradio**: Used to create the interactive web interface.
- **Diffusers**: Utilized for loading and running the Stable Diffusion model.
- **Stable Diffusion Model**: The model used is `runwayml/stable-diffusion-v1-5`, which is a powerful text-to-image generation model.

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