from telegram import Update
from telegram.ext import filters, MessageHandler, ContextTypes

from db.record_new_message import new_message_into_history_for_existing_user
from telegramBot.send_message import send_message
from translate.translate import translate_text
from utils.validation import validate_msg_in_lang

from openaiAPI.ask_chat_GPT import ask_ChatGPT


async def handle_regular_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # get original message
    chat_id = update.effective_chat.id
    input_text = update.message.text
    # validate that the message is in english/russian
    if validate_msg_in_lang(input_text, "ru") or validate_msg_in_lang(input_text, "en"):
        # update user with a new message
        await new_message_into_history_for_existing_user(chat_id, role="user", message=input_text)
        # feed the message to a ChatCompletion API
        chatGPT_response = await ask_ChatGPT(chat_id)
        # translate the response back to russian
        output_text = translate_text("ru", chatGPT_response)
        # update user with a new message
        await new_message_into_history_for_existing_user(chat_id, role="assistant", message=output_text)
    else:
        output_text = "Это сообщение не на русском/английском языках! Пожалуйста, введите сообщение на русском или английском языках!"

    await send_message(update, context, text=output_text)


regular_message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), handle_regular_message)
