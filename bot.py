import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Встав сюди свій токен від BotFather
API_TOKEN = '8033099010:AAHl4qBeu7iM6yJVc05Ti6iLY1nzZLQhFCs'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Обробка команди /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привіт! Я твій новий бот. Напиши мені щось!")

# Ехо-відповідь на будь-яке текстове повідомлення
@dp.message()
async def echo_message(message: types.Message):
    await message.answer(f"Ти сказав: {message.text}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())