from aiogram import Bot, Dispatcher, executor, types
from config import token
import random

bot = Bot(token=token)
dp = Dispatcher(bot)

num = random.randint(1, 3)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer("Я загодал число от 1 до 3")


@dp.message_handler()
async def play(message: types.Message):
    if int(message.text) == num:
        await message.answer_photo(
            "https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg"
        )
    else:
        await message.answer_photo(
            "https://media.makeameme.org/created/sorry-you-lose.jpg"
        )

executor.start_polling(dp)