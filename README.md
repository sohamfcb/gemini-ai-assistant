# Gemini AI Assistant

## Overview

Gemini Vision is an interactive chatbot application that leverages the power of the Gemini AI model to provide insightful responses to user queries. The application allows users to interact with the chatbot via text input, and it can also process images for additional context in generating responses.

## Features

- **Chat Interface:** Users can input text questions and receive responses from the Gemini model in real time.
- **Image Processing:** Users can upload images to receive contextual responses based on visual input.
- **Chat History:** The application maintains a chat history, allowing users to view past interactions.

## Technologies Used

- **Streamlit:** A framework for building web applications in Python, enabling a user-friendly interface.
- **Google Generative AI (Gemini):** An advanced language model for generating human-like text responses.
- **PIL (Pillow):** A Python Imaging Library used for image processing tasks.
- **dotenv:** A library for loading environment variables from a `.env` file.

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sohamfcb/gemini-ai-assistant.git
   cd gemini-ai-assistant
   git clone https://github.com/sohamfcb/gemini-ai-assistant.git
   cd gemini-ai-assistant

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv myvenv
   source myvenv/bin/activate  # On Windows use `myvenv\Scripts\activate`

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt

4. **Set up environment variables:** Create a .env file in the project root and add your Google API key:
   ```bash
   GOOGLE_API_KEY=your_api_key_here

5. **Run the application:**
   ```bash
   streamlit run app.py

## Usage

1. **Chatting with the Bot:**

- Enter your question in the text input field and click the send button (➡️).
- The chatbot will respond with relevant information based on your query.

2. **Image Upload:**

- Use the image uploader to submit an image.
- Optionally, you can ask a question related to the image in the provided text area.
- The bot will analyze the image and respond accordingly.

3. **Viewing Chat History:**

- All interactions will be displayed under the "Chat History" section, showing both user queries and bot responses.
