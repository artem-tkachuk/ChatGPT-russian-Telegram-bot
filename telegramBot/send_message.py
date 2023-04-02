from telegram import Update
from telegram.ext import ContextTypes


async def send_message(update: Update, context: ContextTypes.DEFAULT_TYPE, text: str):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text
    )