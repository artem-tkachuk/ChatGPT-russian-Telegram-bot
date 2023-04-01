import asyncio
import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

from dotenv import load_dotenv
load_dotenv()

token = os.environ.get("TOKEN")


# async def main():
#     bot = telegram.Bot(token)
#     async with bot:
#         # print(
#         #     (await bot.get_updates())[0]
#         # )
#
#         translated_output = translate_text("ru", "Hello, world!")
#
#         await bot.send_message(chat_id=48018875, text="Hello, world!")
#
#
# if __name__ == '__main__':
#     asyncio.run(main())


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Привет! С помощью этого бота ты можешь общаться с ChatGPT на русском :)"
    )


if __name__ == '__main__':
    application = ApplicationBuilder().token(token).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling()







