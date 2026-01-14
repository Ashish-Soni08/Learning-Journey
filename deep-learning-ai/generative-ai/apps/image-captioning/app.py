import base64

import gradio as gr
import io

from PIL import Image

import spaces

from transformers import pipeline

def image_to_base64_str(pil_image: Image.Image) -> str:
    """
    Converts a PIL image to a base64 encoded string.
    Args:
        pil_image (Image.Image): The PIL image to be converted.
    Returns:
        str: The base64 encoded string representation of the image.
    """
    byte_arr = io.BytesIO()
    pil_image.save(byte_arr, format='PNG')
    byte_arr = byte_arr.getvalue()
    return str(base64.b64encode(byte_arr).decode('utf-8'))


# Initialize Model
get_completion = pipeline("image-to-text",model="Salesforce/blip-image-captioning-base", device=0)

@spaces.GPU(duration=120)
def captioner(input: Image.Image) -> str:
    """
    Generate a caption for the given image using the BLIP-IMAGE-CAPTIONING-BASE model.
    Args:
        input (Image.Image): The input image for which to generate a caption.
    Returns:
        str: The generated caption text.
    """
    base64_image = image_to_base64_str(input)
    output = get_completion(base64_image)
    return output[0]['generated_text']

####### GRADIO APP #######
title = """<h1 id="title"> Image Captioning with BLIP model </h1>"""

description = """
- The model used for Generating Captions [BLIP-IMAGE-CAPTIONING-BASE](https://huggingface.co/Salesforce/blip-image-captioning-base).
"""

css = '''
h1#title {
  text-align: center;
}
'''

theme = gr.themes.Soft()
demo = gr.Blocks(css=css, theme=theme)

with demo:
  gr.Markdown(title)
  gr.Markdown(description)
  interface = gr.Interface(fn=captioner,
                    inputs=[gr.Image(label="Upload image", type="pil")],
                    outputs=[gr.Textbox(label="Caption")],
                    allow_flagging="never",
                    examples= "example_images")

demo.launch()