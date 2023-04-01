from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Бот не знает этой команды!"
    )


unknown_handler = MessageHandler(filters.COMMAND, unknown)
