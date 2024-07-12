import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.exceptions import TelegramAPIError
from dotenv import load_dotenv
from keyboard import get_start_keyboard
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from callback_handler import callback_router

load_dotenv()

BOT_TOKEN = os.getenv('API_KEY')


logging.basicConfig(level=logging.INFO)


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
dp.include_router(callback_router)

# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Обновляем интерфейс...", reply_markup=ReplyKeyboardRemove())
    await message.answer("Приветствую! Я бот +7Доставки. Расскажу, как бесплатно получать товары с "
        "<a href='https://www.ozon.ru/'>топового маркетплейса РФ</a>.", reply_markup= get_start_keyboard(),
        parse_mode="HTML")


# Функция для удаления вебхука
async def delete_webhook():
    try:
        await bot.delete_webhook()
        logging.info("Вебхук успешно удален")
    except TelegramAPIError as e:
        logging.error(f"Ошибка при удалении вебхука: {e}")

# Функция запуска бота
async def main():
    # Удаляем вебхук перед запуском бота
    await delete_webhook()
    # Запускаем бота
    try:
        await dp.start_polling(bot)
    except TelegramAPIError as e:
        logging.error(f"Ошибка при запуске бота: {e}")

if __name__ == "__main__":
    asyncio.run(main())