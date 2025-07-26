import chainlit as cl
from src.llm import ask_order, messages

@cl.on_message
async def main(message: cl.Message):
    # Append user message to the message list
    messages.append({"role": "user", "content": message.content})

    # Get response from OpenAI
    response = ask_order(messages)

    # Append assistant response to the message list
    messages.append({"role": "assistant", "content": response})

    # Send a response back to the user
    await cl.Message(content=response).send()
