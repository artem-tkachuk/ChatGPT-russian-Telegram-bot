from telegram.ext import Application
from handlers.handle_start import start_command_handler
from handlers.new_chat import new_chat_handler
from handlers.regular_message import regular_message_handler
from handlers.non_textual_message import non_textual_message_handler
from handlers.unknown import unknown_command_handler


def register_handlers(application: Application):
    application.add_handler(start_command_handler)
    application.add_handler(new_chat_handler)
    application.add_handler(regular_message_handler)
    application.add_handler(non_textual_message_handler)
    application.add_handler(unknown_command_handler)
