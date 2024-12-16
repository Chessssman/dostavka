import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ContentType, Message
from aiogram.filters.command import Command
from aiogram.exceptions import TelegramAPIError
from dotenv import load_dotenv
from keyboard import get_start_keyboard, get_partner_keyboard
from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardRemove
from callback_handler import callback_router
import pandas as pd
from geopy.distance import geodesic
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import keep_alive
from support_handler import callback_router as support_router

load_dotenv()

BOT_TOKEN = os.getenv('API_KEY')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
dp.include_router(callback_router)
dp.include_router(support_router)
df = pd.read_excel('map.xlsx')
router = Router()

# ID чата техподдержки (замените на реальный)
SUPPORT_CHAT_ID = -1002296401929
PARTNER_CHAT_ID = -4767505087  # ID чата для заявок


# Состояния для FSM
class PartnerApplicationState(StatesGroup):
    waiting_for_full_name = State()
    waiting_for_phone = State()
    waiting_for_address = State()
    waiting_for_photos = State()


# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Обновляем интерфейс...", reply_markup=ReplyKeyboardRemove())
    await message.answer("Приветствую! Я бот +7Доставки. Расскажу, как бесплатно получать товары с "
                         "<a href='https://www.ozon.ru/'>топового маркетплейса РФ</a>.",
                         reply_markup=get_start_keyboard(), parse_mode="HTML")


@dp.callback_query(lambda c: c.data == "open_main")
async def process_open_main(callback: types.CallbackQuery):
    await callback.answer()  # Отвечаем на callback, чтобы убрать "часики" у кнопки
    await callback.message.answer("Обновляем интерфейс...", reply_markup=ReplyKeyboardRemove())
    await callback.message.answer(
        "Приветствую! Я бот +7Доставки. Расскажу, как бесплатно получать товары с "
        "<a href='https://www.ozon.ru/'>топового маркетплейса РФ</a>.",
        reply_markup=get_start_keyboard(),
        parse_mode="HTML"
    )


# Обработчик кнопки "Как стать партнером?"
@dp.callback_query(lambda c: c.data == "partner_info")
async def partner_info(callback: types.CallbackQuery):
    info_text = (
        "Компания +7Доставка активно развивает партнерскую сеть Пунктов выдачи заказов на новых территориях и в Крыму.\n\n"
        "Мы готовы рассмотреть Вас как потенциального партнера, если:\n"
        "- У вас есть помещение с большой проходимостью\n"
        "- Вы готовы применить наш брендбук для большей узнаваемости в городе\n"
        "- Имеете представление о работе Пункта Выдачи\n"
        "- Есть желание повышать узнаваемость совместно с нами\n\n"
        "Наши минимальные требования:\n"
        "- Площадь помещения от 30 кв. м\n"
        "- Первый этаж, удобный заход\n"
        "- Наличие рабочего места с ПК, интернета, стеллажей для склада посылок\n"
        "- Аккуратность в работе\n"
        "- Содержание пункта выдачи в чистоте и порядке\n\n"
        "Если вы подходите, нажмите на кнопку \"Подать заявку\" ниже."
    )
    await callback.message.answer(info_text, reply_markup=get_partner_keyboard(), parse_mode="HTML")


# Начало подачи заявки
@dp.callback_query(lambda c: c.data == "submit_application")
async def start_application(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Пожалуйста, укажите ваше ФИО.")
    await state.set_state(PartnerApplicationState.waiting_for_full_name)


# Сбор данных заявки
@dp.message(PartnerApplicationState.waiting_for_full_name)
async def get_full_name(message: types.Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    await message.answer("Спасибо! Теперь укажите ваш номер телефона.")
    await state.set_state(PartnerApplicationState.waiting_for_phone)


@dp.message(PartnerApplicationState.waiting_for_phone)
async def get_phone(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("Отлично! Укажите адрес вашего помещения.")
    await state.set_state(PartnerApplicationState.waiting_for_address)


@dp.message(PartnerApplicationState.waiting_for_address)
async def get_address(message: types.Message, state: FSMContext):
    await state.update_data(address=message.text)
    await message.answer("Почти готово! Пожалуйста, отправьте фото или видео помещения (включая фасад).")
    await state.set_state(PartnerApplicationState.waiting_for_photos)


@dp.message(PartnerApplicationState.waiting_for_photos, content_types=[ContentType.PHOTO, ContentType.VIDEO])
async def get_photos(message: types.Message, state: FSMContext):
    data = await state.get_data()

    # Отправка данных в чат
    application_text = (
        f"Новая заявка от потенциального партнера:\n"
        f"ФИО: {data['full_name']}\n"
        f"Телефон: {data['phone']}\n"
        f"Адрес помещения: {data['address']}\n"
    )
    await bot.send_message(PARTNER_CHAT_ID, application_text)

    # Пересылка медиа
    if message.photo:
        await message.photo[-1].send_to(PARTNER_CHAT_ID)
    elif message.video:
        await message.video.send_to(PARTNER_CHAT_ID)

    await message.answer("Спасибо! Ваша заявка отправлена. Мы свяжемся с вами в ближайшее время.")
    await state.clear()


dp.include_router(router)


# Функция запуска бота
async def main():
    # Удаляем вебхук перед запуском бота
    try:
        await bot.delete_webhook()
        logging.info("Вебхук успешно удален")
    except TelegramAPIError as e:
        logging.error(f"Ошибка при удалении вебхука: {e}")

    # Запускаем бота
    try:
        await dp.start_polling(bot)
    except TelegramAPIError as e:
        logging.error(f"Ошибка при запуске бота: {e}")


if __name__ == "__main__":
    keep_alive.keep_alive()
    asyncio.run(main())
