import streamlit as st
import google.generativeai as genai
import os
from PIL import Image

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel('gemini-1.5-pro-exp-0801')

def getGeminiResponse(user_input,image,prompt):
    response=model.generate_content([user_input,image[0],prompt])
    return response


def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

st.set_page_config(page_title='Inv Ext')
st.header('Gemini Multi-Language Invoice Extractor')

user_input=st.text_area('Prompt: ',key='input')
uploaded_file=st.file_uploader('Select an Invoice:',type=['jpeg','jpg','png','webp'])

image=''

if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image=image,caption='Uploaded Image',use_column_width=True)

btn=st.button('Submit')

input_prompt = """
               You are an expert in understanding invoices.
               You will receive input images as invoices &
               you will have to answer questions based on the input image
               """

if btn:
    image_data=input_image_setup(uploaded_file=uploaded_file)
    response=getGeminiResponse(user_input=input_prompt,
                               image=image_data,
                               prompt=user_input)
    st.subheader('Response')
    st.markdown(response.text)