from db.get_user import find_user
from db.mongo import get_mongo_db
from translate.translate import translate_text
import os


async def get_translated_messages(chat_id):
    database = get_mongo_db()
    # Get collection
    collection_name = os.environ.get('MONGO_DB_COLLECTION_NAME')
    collection = database[collection_name]
    # get user
    user = await find_user(chat_id)
    messages = user['chats'][-1]

    translated_messages = []

    for message in messages:
        translated_message = translate_text("en", message['content'])

        translated_messages.append({
            "role": message['role'], 
            "content": translated_message
        })

    return translated_messages
