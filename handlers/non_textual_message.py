from telegram.ext import MessageHandler, filters

from telegramBot.send_message import send_message


async def handle_non_textual_message(update, context):
    await send_message(update, context, text="Бот на данный момент умеет работать исключительно с текстом!")


non_textual_message_handler = MessageHandler(~filters.TEXT, handle_non_textual_message)
