# Text Summarization App

This application provides a simple interface to summarize text using a pre-trained model from Hugging Face's Transformers library. The model used under the hood is `DISTILBART-12-6-CNN`, a distilled version of BART fine-tuned on the CNN/Daily Mail dataset.

## Features
- **Text Summarization**: Generate concise summaries of input text.
- **User-Friendly Interface**: Built using Gradio for an easy-to-use web interface.

## Model
- **Model Used**: `DISTILBART-12-6-CNN`
- **Framework**: Hugging Face Transformers

## Software Packages

- **Gradio**: Used to create the web interface.
- **Transformers**: Used for model inference.
- **Spaces**: Utilized for GPU acceleration during model execution.

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
