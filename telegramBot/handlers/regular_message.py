from telegram import Update
from telegram.ext import filters, MessageHandler, ContextTypes

# async def main():
#     bot = telegramBot.Bot(token)
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

async def regular_message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=update.message.text
    )

regular_message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), regular_message_handler)