from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters
from telegramBot.send_message import send_message


async def handle_unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text
    await send_message(update, context, text="Бот не знает этой команды!")


unknown_command_handler = MessageHandler(filters.COMMAND, handle_unknown_command)
