from telegram import Update
from telegram.ext import CommandHandler, ContextTypes


async def new_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # TODO implement resetting message history with OpenAI
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=update.message.text
    )


new_chat_handler = CommandHandler('new_chat', new_chat)
