from dotenv import load_dotenv
from telegramBot.bot import configure_bot
from db.mongo import get_mongo_db

load_dotenv()

if __name__ == '__main__':
    application = configure_bot()
    # test database connection
    db = get_mongo_db()
    # launch the bot
    application.run_polling()
