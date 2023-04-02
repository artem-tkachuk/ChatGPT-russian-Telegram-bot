from db.mongo import get_mongo_db
import os


async def find_user(chat_id: str):
    # Setup MongoDB to store chat history and user data
    database = get_mongo_db()
    # Get collection
    collection_name = os.environ.get('MONGO_DB_COLLECTION_NAME')
    collection = database[collection_name]
    # get document
    return collection.find_one({"chat_id": chat_id})
