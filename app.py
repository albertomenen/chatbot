from flask import Flask, request, render_template
import openai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('CHAT_API_KEY')
openai.api_key = api_key

app = Flask(__name__)

def chat_with_gpt3(message):
    response = openai.Completion.create(
        engine="text-davinci-003", 
        prompt=message, 
        max_tokens=150
    )
    return response.choices[0].text.strip()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get')
def get_bot_response():
    user_text = request.args.get('msg')
    return chat_with_gpt3(user_text)

if __name__ == "__main__":
    app.run(port=5000)
