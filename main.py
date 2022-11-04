from aiogram import Bot,Dispatcher,executor,types
from api import api

BOT_TOKEN = 'API_TOKEN here'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)

dollar = api()

@dp.message_handler(commands=['start'])
async def first_handler(message:types.Message):
    await message.answer(f' Assalomu alaykum \n Exchange-Rate botimizga xush kelibsiz! \n Hozirda 1$ - {dollar} som')

@dp.message_handler(commands=['help'])
async def help_handler(message:types.Message):
    await message.answer("Bu bo'timiz sizga Dollarning hozirgi vaqtdagi o'zbek sommida qancha bo'lishini aniqlab beradi!")

@dp.message_handler(content_types='text')
async def exchange(message:types.Message):
    kirit = message.text
    try:
        await message.answer(f'{kirit} $ o\'zbek so\'mida - {str(dollar*float(kirit))} turadi!')
    except ValueError:
        await message.answer(f'Iltimos raqam kiriting !')
    # print(float(kirit))


if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)