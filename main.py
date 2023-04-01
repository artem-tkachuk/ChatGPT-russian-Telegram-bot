from dotenv import load_dotenv
from telegramBot.bot import configure_bot

load_dotenv()

if __name__ == '__main__':
    application = configure_bot()
    # launch the bot
    application.run_polling()


