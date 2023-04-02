# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
import os
from openaiAPI.get_messages import get_translated_messages


async def ask_ChatGPT(chat_id):
    # initialize ChatGPT
    openai.api_key = os.getenv("OPENAI_API_KEY")
    # get messages
    translated_messages = await get_translated_messages(chat_id)
    # ask
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=translated_messages
    )

    return response.choices[0].message.content
