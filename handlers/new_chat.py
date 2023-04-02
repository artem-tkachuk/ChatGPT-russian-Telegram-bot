from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

from db.start_new_chat import start_new_chat
from telegramBot.send_message import send_message


async def handle_new_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # implement resetting message history with OpenAI
    chat_id = update.effective_chat.id
    await start_new_chat(chat_id)
    # TODO ur helpful assist
    await send_message(update, context, text="====================\nНовый чат начат!\n====================")


new_chat_handler = CommandHandler('newchat', handle_new_chat)
