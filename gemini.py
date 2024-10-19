import os
from dotenv import load_dotenv
import google.generativeai as genai
import time
import sys

# Load environment variables from .env file
load_dotenv()

# Configure Gemini API with the API key from the .env file
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Create the model instance
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# Start a chat session
chat_session = model.start_chat(history=[])

# Chat with the model in a loop
print("Start chatting with Gemini! (type 'exit' to quit)\n")

while True:
    # Get user input
    user_input = input("You: ")

    # Exit condition
    if user_input.lower() == "exit":
        print("Ending chat. Goodbye!")
        break

    # Send the message to Gemini
    response = chat_session.send_message(user_input)

    # Print the response from Gemini with typing animation
    print("Gemini: ", end="")
    for char in response.text:
        print(char, end="")
        sys.stdout.flush()
        time.sleep(0.01)  # Adjust typing speed here
    print("\n")
