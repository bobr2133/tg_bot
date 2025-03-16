from aiogram import Bot, Dispatcher, F, types
from aiogram.filters.command import Command
from random import randint
import asyncio  
from dotenv import dotenv_values

config = dotenv_values()
bot = Bot(token=config["TOKEN"])
dp = Dispatcher()
asnwers = ["2202 2067 3891 8889, сбербанк"]
@dp.message(Command("start"))
async def cmd_start(message):
    await message.reply('Привет! дай денег')
@dp.message(F.text)
async def asd(message):
    answers = ["2202 2067 3891 8889, сбербанк"]
    await message.reply(answers[randint(0,len(answers)-1)])
async def main():
    await dp.start_polling(bot)

asyncio.run(main())