from telegram import Update
from telegram.ext import filters, MessageHandler, ContextTypes
from translate.translate import translate_text
from utils.validation import validate_msg_in_lang

from openaiAPI.ask_chat_GPT import ask_ChatGPT


async def regular_message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # get original message
    input_text = update.message.text
    # validate that the message is in english/russian
    if validate_msg_in_lang(input_text, "ru") or validate_msg_in_lang(input_text, "en"):
        # translate the input message to english for ChatGPT API
        en_input_text = translate_text("en", input_text)
        # feed the message to a ChatCompletion API
        chatGPT_response = ask_ChatGPT(en_input_text)
        # translate the response back to russian
        output_text = translate_text("ru", chatGPT_response)
    else:
        output_text = "Это сообщение не на русском/английском языках! Пожалуйста, введите сообщение на русском или английском языках!"

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=output_text
    )


regular_message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), regular_message_handler)
