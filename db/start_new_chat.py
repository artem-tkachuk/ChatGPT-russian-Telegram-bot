from db.get_user import find_user
from db.mongo import get_mongo_db
import os


async def start_new_chat(chat_id: int):
    database = get_mongo_db()
    # Get collection
    collection_name = os.environ.get('MONGO_DB_COLLECTION_NAME')
    collection = database[collection_name]
    # get user
    user = await find_user(chat_id)
    chats = user['chats']

    chats.append([{"role": "system", "content": "You are a helpful assistant."}])

    collection.update_one(
        {"chat_id": chat_id},
        {"$set": {"chats": chats}
     })