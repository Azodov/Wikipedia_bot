import logging
import wikipedia
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '2134514498:AAHEgKNZRCLmJEyUSQ3VzPtrmWu9VNt_qpc'
wikipedia.set_lang('uz')

#configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatche
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Siz so'ragan mavzudagi maqola va malumotlarni sizga qaytarib jo'nataman")


@dp.message_handler()
async def sendwiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer('Bu mavzuga oid maqola topilmadi')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)