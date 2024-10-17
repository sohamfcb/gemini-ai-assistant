import streamlit as st

st.set_page_config(page_title='Gemini Lens: See, Ask, Understand')
st.header('Gemini Lite: AI-Powered Q&A and Image Analysis')

st.image('final_keyword_header.width-1600.format-webp.webp')

st.markdown('''
   # Gemini Models Overview

Gemini models are a series of advanced AI models developed by Google, designed for natural language processing (NLP), image recognition, and multimodal tasks. These models leverage cutting-edge machine learning techniques to generate human-like text responses, analyze images, and combine both modalities for richer interactions.

## Key Features of Gemini Models

- **Multimodal Capabilities**: Gemini can process and generate both text and images, allowing for more interactive and versatile applications.
- **High-Quality Text Generation**: The models excel at understanding context and generating coherent, contextually relevant responses.
- **Robust API**: The Gemini API provides seamless access to the models, making it easy to integrate their capabilities into various applications.

## Building LLM Projects with Gemini APIs

### 1. **Setting Up the Environment**
To get started with Gemini models, ensure you have the following:
- An active Google Cloud account
- Your API key from the Google Cloud Console
- Required Python packages, including `google-generativeai`

### 2. **Using the API**
You can interact with the Gemini models via the API by making requests for text generation, image analysis, or multimodal responses. Here’s a simple example of how to use the API:

```python
from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-1.5-pro-exp-0801')

# Text Generation Example
response = model.generate_content("What is the significance of AI?")
print(response.text)

# Image Analysis Example
response = model.generate_content(image=your_image)
print(response.text)
''')