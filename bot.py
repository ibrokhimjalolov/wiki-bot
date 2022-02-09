import logging, asyncio, wiki
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5137083379:AAHk650lJgI7uc8dga0yI3nTuo4QWAq0ScI'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

async def process_wiki_async(message: types.Message, del_message: types.Message):
    ans = wiki.searchWiki(message.text)
    await del_message.delete()
    await asyncio.sleep(0.5)
    await message.reply(ans)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(f"Salom {message.from_user.full_name}! Wikipeida Botiga xush kelibsiz")


@dp.message_handler()
async def sendWiki(message: types.Message):
    del_msg = await message.reply("🔎")
    asyncio.create_task(process_wiki_async(message, del_msg))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
