# from dotenv import load_dotenv
# load_dotenv()

# import streamlit as st
# import os
# import google.generativeai as genai
# import textwrap
# from PIL import Image, ExifTags

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# model=genai.GenerativeModel('gemini-1.5-pro-exp-0801')

    
# def getGeminiImageResponse(image,input_query):
#     if input_query:
#         response=model.generate_content([input_query,image])
#     else:
#         response=model.generate_content(image)
#     return response.text

# def correct_image_orientation(img):
#     try:
#         for orientation in ExifTags.TAGS.keys():
#             if ExifTags.TAGS[orientation] == 'Orientation':
#                 break
#         exif = img._getexif()
#         if exif is not None:
#             orientation_value = exif.get(orientation)
#             if orientation_value == 3:
#                 img = img.rotate(180, expand=True)
#             elif orientation_value == 6:
#                 img = img.rotate(270, expand=True)
#             elif orientation_value == 8:
#                 img = img.rotate(90, expand=True)
#     except (AttributeError, KeyError, IndexError):
#         # Cases: image don't have getexif
#         pass
#     return img
    
# def to_markdown(text):
#     text = text.replace('•', '  *')
#     return textwrap.indent(text, '> ', predicate=lambda _: True)

# st.set_page_config(page_title='Gemini Vision')
# st.header('Gemini Vision')

# image_input=st.file_uploader('Choose an image',type=['jpg','jpeg','png','webp'])
# user_input_image=st.text_area('Ask your Question (if you have any) ',height=20,key='input_image')

# btn2=st.button(label='📤',key='image')

# if btn2:
#     if image_input:
#         img=Image.open(image_input)
#         img=correct_image_orientation(img)
#         response=getGeminiImageResponse(image=img,input_query=user_input_image)
#         st.image(image=img,caption='Uploaded Image',width=500)
#         response=to_markdown(response)
#         st.markdown(response)

#     else:
#         st.error('Please provide an Image')


from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
import textwrap
from PIL import Image, ExifTags

# Configure the Google Generative AI model with the API key from environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-1.5-pro-exp-0801')

def getGeminiImageResponse(image, input_query):
    """
    Generate a response from the Gemini model based on the input image and query.

    Parameters:
    - image: The uploaded image.
    - input_query: A string query from the user.

    Returns:
    - response.text: The generated response text from the model.
    """
    try:
        if input_query:
            response = model.generate_content([input_query, image])
        else:
            response = model.generate_content(image)
        return response.text
    except Exception as e:
        # Log the error for debugging
        st.error(f"An error occurred while generating response: {str(e)}")
        return "Couldn't fetch what you asked for."

def correct_image_orientation(img):
    """
    Correct the orientation of the uploaded image based on EXIF data.

    Parameters:
    - img: The uploaded image.

    Returns:
    - img: The corrected image.
    """
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break
        exif = img._getexif()
        if exif is not None:
            orientation_value = exif.get(orientation)
            if orientation_value == 3:
                img = img.rotate(180, expand=True)
            elif orientation_value == 6:
                img = img.rotate(270, expand=True)
            elif orientation_value == 8:
                img = img.rotate(90, expand=True)
    except (AttributeError, KeyError, IndexError):
        # Cases: image doesn't have EXIF data
        pass
    return img
    
def to_markdown(text):
    """
    Convert the given text to markdown format.

    Parameters:
    - text: The input text to be converted.

    Returns:
    - The formatted markdown text.
    """
    text = text.replace('•', '  *')
    return textwrap.indent(text, '> ', predicate=lambda _: True)

# Streamlit page configuration
st.set_page_config(page_title='Gemini Vision')
st.header('Gemini Vision')

# User image upload area
image_input = st.file_uploader('Choose an image', type=['jpg', 'jpeg', 'png', 'webp'])
user_input_image = st.text_area('Ask your Question (if you have any)', height=20, key='input_image')

# Button for submission
btn2 = st.button(label='📤', key='image')

if btn2:
    if image_input:
        try:
            # Open the uploaded image and correct its orientation
            img = Image.open(image_input)
            img = correct_image_orientation(img)

            # Get response from the model based on the uploaded image and user input
            response = getGeminiImageResponse(image=img, input_query=user_input_image)

            # Display the uploaded image and the model's response
            st.image(image=img, caption='Uploaded Image', width=500)
            response = to_markdown(response)
            st.markdown(response)
        except Exception as e:
            # Handle any errors that occur during processing
            st.error(f"An error occurred while processing your request: {str(e)}")
    else:
        # Error message for empty image input
        st.error('Please provide an Image')
