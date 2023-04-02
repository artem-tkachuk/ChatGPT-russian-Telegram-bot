from telegram import Update
from db.mongo import get_mongo_db, check_user_existence
import os


async def register_new_user(update: Update):
    new_user_object = {
        # User attributes
        "first_name": update.effective_user.first_name,
        "last_name": update.effective_user.last_name,
        "id": update.effective_user.id,
        "username": update.effective_user.username,
        "chat_id": update.effective_message.chat_id,
        "user_is_tg_premium": update.effective_user.is_premium,
        # "language_code": update.effective_user.language_code,  # Maybe add this later
        "is_bot": update.effective_user.is_bot,
        "link": update.effective_user.link,
        # Message attributes
        "is_command": update.effective_message.entities[0].type == "bot_command",
        "is_text": update.effective_message.entities[0].type in ["text", "bot_command"],
        "is_known_command": update.effective_message.entities[0].type == "bot_command" and update.effective_message.text in ["/start", "/newchat"],
        "datetime": update.effective_message.date,
        "chats": [
            [
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": '/start'}
            ]
        ]
    }

    # Setup new MongoDB object to store chat history and user data
    database = get_mongo_db()
    # Get collection
    collection_name = os.environ.get('MONGO_DB_COLLECTION_NAME')
    collection = database[collection_name]
    # insert document
    collection.insert_one(new_user_object)
    print(f"New user registered: {new_user_object['username']}")
