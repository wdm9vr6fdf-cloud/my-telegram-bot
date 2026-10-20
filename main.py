import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Токен мы будем брать из переменной окружения, а не писать прямо тут
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "👋 Привет! Напиши название товара, место встречи и время — я всё соберу в готовое сообщение.\n\n"
        "Сначала просто напиши: <название товара>"
    )

# Здесь можно расширять логику: сохранять ответы, отправлять тебе и т.д.
# Для начала достаточно этого минимума.

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
