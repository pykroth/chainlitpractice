from openai import OpenAI
from src.prompt import system_introduction
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OpenAI_API_Key"))  # Keep only this line

messages = [
   {"role": "system", "content": system_introduction}
]

def ask_order(message, model="gpt-3.5-turbo", temperature=0):
   response = client.chat.completions.create(
      model=model,
      messages=message,  # Use the passed argument, not always the global `messages`
      temperature=temperature
   )
   return response.choices[0].message.content
