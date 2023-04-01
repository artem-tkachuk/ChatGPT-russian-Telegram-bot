from telegram import Update
from telegram.ext import ContextTypes, CommandHandler


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Привет! С помощью этого бота ты можешь общаться с ChatGPT на русском прямо в Telegram :) \nБот отвечает только на текстовые сообщения!"
    )


start_handler = CommandHandler('start', start)
