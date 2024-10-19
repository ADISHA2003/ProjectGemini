# Gemini Chatbot

This is a simple command-line chatbot that uses Google's Gemini API to generate responses. 

## Features

- **Interactive chat:** Engage in a conversation with the Gemini model.
- **Typing animation:** The chatbot's responses are displayed with a typing animation for a more engaging experience.

## Requirements

- **Python 3.6 or higher**
- **`google-generativeai` package:** Install using `pip install google-generativeai`
- **`python-dotenv` package:** Install using `pip install python-dotenv`
- **Gemini API Key:** 
    - Obtain an API key from [https://developers.generativeai.google.com/](https://developers.generativeai.google.com/)
    - Create a `.env` file in the project directory and add the following line, replacing `YOUR_API_KEY` with your actual API key:
      ```
      GEMINI_API_KEY=YOUR_API_KEY
      ```

## How to Run

```bash
python gemini.py
```