from telegramBot.handlers.start import start_handler
from telegramBot.handlers.regular_message import regular_message_handler
from telegramBot.handlers.new_chat import new_chat_handler
from telegramBot.handlers.unknown import unknown_handler
from telegram.ext import Application


def register_handlers(application: Application):
    application.add_handler(start_handler)
    application.add_handler(new_chat_handler)
    application.add_handler(regular_message_handler)
    application.add_handler(unknown_handler)
