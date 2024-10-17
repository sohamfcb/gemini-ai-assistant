# from dotenv import load_dotenv
# load_dotenv()

# import streamlit as st
# import os
# import google.generativeai as genai
# import textwrap
# from PIL import Image

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# model=genai.GenerativeModel('gemini-1.5-pro-exp-0801')
# chat=model.start_chat(history=[])

# def getGeminiResponse(question):
#     response=chat.send_message(question)
#     return response

# st.set_page_config(page_title='Chatbot')
# st.header('Gemini Chatbot')

# if 'chat_history' not in st.session_state:
#     st.session_state['chat_history']=[]

# user_input=st.text_input('Text: ',key='input')
# send_btn=st.button('➡️',key='chat')

# if send_btn and user_input:
#     response=getGeminiResponse(question=user_input)
#     st.session_state['chat_history'].append(('You ',user_input))

#     st.write(response.text)
#     st.session_state['chat_history'].append(('Gemini ',response.text))

# st.subheader('Chat History')

# for role,text in st.session_state['chat_history']:
#     st.write(f'{role}: {text}')


from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
import textwrap
from PIL import Image

# Configure the Google Generative AI model with the API key from environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the Gemini model for chat functionality
model = genai.GenerativeModel('gemini-1.5-pro-exp-0801')
chat = model.start_chat(history=[])

def getGeminiResponse(question):
    """
    Send a question to the Gemini chatbot and receive a response.

    Parameters:
    - question: The user's input question.

    Returns:
    - The response from the Gemini chatbot.
    """
    try:
        response = chat.send_message(question)
        return response
    except Exception as e:
        # Log the error for debugging
        st.error(f"An error occurred while fetching the response: {str(e)}")
        return None

# Streamlit page configuration
st.set_page_config(page_title='Chatbot')
st.header('Gemini Chatbot')

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# User input area for text input
user_input = st.text_input('Text: ', key='input')
send_btn = st.button('➡️', key='chat')

if send_btn and user_input:
    response = getGeminiResponse(question=user_input)

    if response:
        # Append user input and chatbot response to the chat history
        st.session_state['chat_history'].append(('You', user_input))
        st.write(response.text)
        st.session_state['chat_history'].append(('Gemini', response.text))

st.subheader('Chat History')

# Display the chat history
for role, text in st.session_state['chat_history']:
    st.write(f'{role}: {text}')
