import openai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('CHAT_API_KEY')
openai.api_key = api_key


def chat_with_gpt3(message):
    response = openai.Completion.create(
        engine="text-davinci-003", 
        prompt=message, 
        max_tokens=150
    )
    return response.choices[0].text.strip()

while True:
    message = input("Tu: ")
    print("Chatbot: ", chat_with_gpt3(message))
