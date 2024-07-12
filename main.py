import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ContentType, Message
from aiogram.filters.command import Command
from aiogram.exceptions import TelegramAPIError
from dotenv import load_dotenv
from keyboard import get_start_keyboard
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from callback_handler import callback_router
import pandas as pd
from geopy.distance import geodesic
from aiogram import Router, F


load_dotenv()

BOT_TOKEN = os.getenv('API_KEY')


logging.basicConfig(level=logging.INFO)


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
dp.include_router(callback_router)
df = pd.read_excel('map.xlsx')
router = Router()

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

def get_nearby_locations(user_location, max_distance_km=2):
    nearby_locations = []

    for index, row in df.iterrows():
        location = (row['широта'], row['долгота'])
        distance = geodesic(user_location, location).kilometers
        if distance <= max_distance_km:
            nearby_locations.append((row['адрес'], distance))
    
    return sorted(nearby_locations, key=lambda x: x[1])

@router.message(F.content_type == ContentType.LOCATION)
async def handle_location(message: Message):
    user_location = (message.location.latitude, message.location.longitude)
    nearby_locations = get_nearby_locations(user_location)

    if nearby_locations:
        response = "Вот ближайшие к вам пункты выдачи:\n"
        for address, distance in nearby_locations:
            response += f"{address} - {distance:.2f} км\n"
    else:
        response = "К сожалению, в радиусе 2 км нет точек."

    await message.reply(response)

dp.include_router(router)

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