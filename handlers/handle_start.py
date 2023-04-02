from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from db.mongo import get_mongo_db, check_user_existence
from db.new_user import register_new_user
from db.record_new_message import new_message_into_history_for_existing_user
from telegramBot.send_message import send_message


async def handle_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    database = get_mongo_db()
    # Check they don't already exist because a user can start a new chat with the bot
    chat_id = update.effective_chat.id
    user_exists = check_user_existence(chat_id)

    if not user_exists:
        # create a new user
        await register_new_user(update)
    # else:
    #     # update user with a new message
    #     await new_message_into_history_for_existing_user(chat_id, "user", "/start")

    await send_message(update, context, text="Привет! С помощью этого бота ты можешь общаться с ChatGPT на русском прямо в Telegram :) \nБот отвечает только на текстовые сообщения!")


start_command_handler = CommandHandler('start', handle_start)
