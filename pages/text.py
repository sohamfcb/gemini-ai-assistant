# from dotenv import load_dotenv
# load_dotenv()

# import streamlit as st
# import os
# import google.generativeai as genai
# import textwrap
# from PIL import Image

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# model=genai.GenerativeModel('gemini-1.5-pro-exp-0801')

# def getGeminiResponse(query: str):

#     try:
#         response=model.generate_content(query)
#         return response.text
    
#     except:
#         return "Couldn't fetch what you asked for."
    
# def getGeminiImageResponse(image,input_query):
#     if input_query:
#         response=model.generate_content([input_query,image])
#     else:
#         response=model.generate_content(image)
#     return response.text
    
# def to_markdown(text):
#     text = text.replace('•', '  *')
#     return textwrap.indent(text, '> ', predicate=lambda _: True)

# st.set_page_config(page_title='Q&A')
# st.header('Gemini Lite')


# user_input=st.text_area('Input: ',height=20,key='input')
# # user_input=st.text_input('Input: ',key='input')

# btn=st.button('📤',key='text')

# if btn:
#     if user_input:
#         response=getGeminiResponse(user_input)
#         response=to_markdown(response)

#         st.markdown(response)

#     else:
#         st.error('Please enter a question or query.')


from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
import textwrap
from PIL import Image

# Configure the Google Generative AI model with the API key from environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-1.5-pro-exp-0801')

def getGeminiResponse(query: str):
    """
    Generate a response from the Gemini model based on the input query.

    Parameters:
    - query: A string input from the user.

    Returns:
    - response.text: The generated response text from the model.
    """
    try:
        response = model.generate_content(query)
        return response.text
    except Exception as e:
        # Log the error for debugging
        st.error(f"An error occurred while generating response: {str(e)}")
        return "Couldn't fetch what you asked for."

def to_markdown(text):
    """
    Convert the given text to markdown format, replacing specific symbols
    for better display.

    Parameters:
    - text: The input text to be converted.

    Returns:
    - The formatted markdown text.
    """
    text = text.replace('•', '  *')
    return textwrap.indent(text, '> ', predicate=lambda _: True)

# Streamlit page configuration
st.set_page_config(page_title='Q&A')
st.header('Gemini Lite')

# User input area
user_input = st.text_area('Input: ', height=20, key='input')

# Button for submission
btn = st.button('📤', key='text')

if btn:
    if user_input:
        try:
            # Get response from the model based on user input
            response = getGeminiResponse(user_input)
            response = to_markdown(response)

            # Display the response in markdown format
            st.markdown(response)
        except Exception as e:
            # Handle any errors that occur during the response generation or display
            st.error(f"An error occurred while processing your request: {str(e)}")
    else:
        # Error message for empty user input
        st.error('Please enter a question or query.')
