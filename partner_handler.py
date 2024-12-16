from aiogram import Router, types
from aiogram.types import ContentType, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import logging

# ID чата для получения заявок
PARTNER_CHAT_ID = -4767505087  # Замените на реальный ID

# Создаем роутер для обработки заявок партнёров
partner_router = Router()

# Состояния для FSM
class PartnerApplicationState(StatesGroup):
    waiting_for_full_name = State()
    waiting_for_phone = State()
    waiting_for_address = State()
    waiting_for_photos = State()

# Клавиатура для кнопки подачи заявки
def get_partner_keyboard():
    buttons = [
        [InlineKeyboardButton(text="Подать заявку", callback_data="submit_application")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

# Обработчик кнопки "Как стать партнером?"
@partner_router.callback_query(lambda c: c.data == "partner_info")
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
@partner_router.callback_query(lambda c: c.data == "submit_application")
async def start_application(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Пожалуйста, укажите ваше ФИО.")
    await state.set_state(PartnerApplicationState.waiting_for_full_name)

# Сбор данных заявки
@partner_router.message(PartnerApplicationState.waiting_for_full_name)
async def get_full_name(message: types.Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    await message.answer("Спасибо! Теперь укажите ваш номер телефона.")
    await state.set_state(PartnerApplicationState.waiting_for_phone)

@partner_router.message(PartnerApplicationState.waiting_for_phone)
async def get_phone(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("Отлично! Укажите адрес вашего помещения.")
    await state.set_state(PartnerApplicationState.waiting_for_address)

@partner_router.message(PartnerApplicationState.waiting_for_address)
async def get_address(message: types.Message, state: FSMContext):
    await state.update_data(address=message.text)
    await message.answer("Почти готово! Пожалуйста, отправьте фото или видео помещения (включая фасад).")
    await state.set_state(PartnerApplicationState.waiting_for_photos)

@partner_router.message(PartnerApplicationState.waiting_for_photos)
async def get_photos(message: types.Message, state: FSMContext):
    data = await state.get_data()

    # Отправка данных в чат
    application_text = (
        f"Новая заявка от потенциального партнера:\n"
        f"ФИО: {data['full_name']}\n"
        f"Телефон: {data['phone']}\n"
        f"Адрес помещения: {data['address']}\n"
    )
    await message.bot.send_message(PARTNER_CHAT_ID, application_text)

    # Пересылка медиа
    if message.photo:
        await message.bot.send_photo(PARTNER_CHAT_ID, photo=message.photo[-1].file_id)
    elif message.video:
        await message.bot.send_video(PARTNER_CHAT_ID, video=message.video.file_id)

    await message.answer("Спасибо! Ваша заявка отправлена. Мы свяжемся с вами в ближайшее время.")
    await state.clear()
