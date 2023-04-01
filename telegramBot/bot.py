import os
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler
from telegramBot.logging_config import setup_logging
from telegramBot.register_handlers import register_handlers


def configure_bot():
    token = os.environ.get("TOKEN")
    # log/track errors if they happen
    setup_logging()
    # create a new application
    application = ApplicationBuilder().token(token).build()
    # register handlers with the application
    register_handlers(application)

    return application
