from db.mongo import get_mongo_db
from db.get_user import find_user
import os


async def new_message_into_history_for_existing_user(chat_id, role, message):
    # Setup MongoDB to store chat history and user data
    database = get_mongo_db()
    # Get collection
    collection_name = os.environ.get('MONGO_DB_COLLECTION_NAME')
    collection = database[collection_name]
    # get user
    user = await find_user(chat_id)
    # Add new message
    user['chats'][-1].append({"role": role, "content": message})
    # # Store document
    collection.update_one(
        {"chat_id": chat_id},
        {"$set": {"chats": user['chats']}
     })
