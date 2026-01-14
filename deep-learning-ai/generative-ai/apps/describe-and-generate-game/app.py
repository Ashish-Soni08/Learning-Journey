import spaces

from diffusers import DiffusionPipeline

import gradio as gr

from PIL import Image

import torch
from transformers import pipeline

# Initialize Caption Generation Model
get_caption = pipeline("image-to-text",model="Salesforce/blip-image-captioning-base", device=0)

# Initialize Image Generation Model
generate_pipeline = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", )
pipe = generate_pipeline.to("cuda")

def captioner(input: Image.Image) -> str:
    """
    Generate a descriptive caption for the given input image using the BLIP-IMAGE-CAPTIONING-BASE model.
    Args:
        input (Image.Image): The input image for which to generate a caption.
    Returns:
        str: The generated caption describing the input image.
    """
    output = get_caption(input)
    return output[0]['generated_text']

def generate(prompt: str) -> Image.Image:
    """
    Generate an image based on the given textual prompt using the Stable Diffusion model.
    Args:
        prompt (str): The textual description based on which to generate an image.
    Returns:
        Image.Image: The generated image corresponding to the given prompt.
    """
    return pipe(prompt).images[0]

@spaces.GPU(duration=300)
def caption_and_generate(image: Image.Image) -> list:
    """
    Generate a caption for the given image and then generate a new image based on that caption.
    Args:
        image (Image.Image): The input image for which to generate a caption and subsequently a new image.
    Returns:
        list: A list containing the generated caption (str) and the generated image (Image.Image).
    """
    caption = captioner(image)
    image = generate(caption)
    return [caption, image]

####### GRADIO APP #######

with gr.Blocks() as demo:
    gr.Markdown("# Describe-and-Generate game 🖍️")
    image_upload = gr.Image(label="Your first image",type="pil")
    btn_all = gr.Button("Caption and generate")
    caption = gr.Textbox(label="Generated caption")
    image_output = gr.Image(label="Generated Image")

    btn_all.click(fn=caption_and_generate, inputs=[image_upload], outputs=[caption, image_output])

demo.launch()