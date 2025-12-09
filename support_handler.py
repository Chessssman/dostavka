# support_handler
import re
from aiogram import Router, types, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

class SupportState(StatesGroup):
    waiting_for_question = State()

callback_router = Router()

# Кнопка "Обратиться в поддержку"
@callback_router.callback_query(lambda c: c.data == "support")
async def support_start(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("🛠 Пожалуйста, опишите вашу проблему (текст, фото или видео).")
    await state.set_state(SupportState.waiting_for_question)

# Получение вопроса
@callback_router.message(SupportState.waiting_for_question)
async def receive_support_question(message: types.Message, state: FSMContext):
    support_chat_id = -1002296401929 

    # 1. Данные пользователя
    user_id = message.from_user.id
    username = message.from_user.username or "нет ника"
    
    # 2. Формируем "шапку"
    header = f"🆔 ID: {user_id}\n👤 От: @{username}\n➖➖➖➖➖\n"

    # 3. Отправка в зависимости от типа контента
    if message.text:
        # Текст
        await message.bot.send_message(support_chat_id, header + message.text)
    else:
        # Медиа (фото/видео)
        original_caption = message.caption or ""
        await message.copy_to(support_chat_id, caption=header + original_caption)

    await message.answer("Ваш вопрос отправлен. Ожидайте ответа.")
    await state.clear()


# Ответ админа пользователю
@callback_router.message()
async def forward_support_response(message: types.Message):
    if message.chat.id == -1002296401929: # ID чата поддержки
        if message.reply_to_message:
            # Извлекаем текст из исходного сообщения
            original_text = message.reply_to_message.text or message.reply_to_message.caption or ""
            
            # Ищем ID
            match = re.search(r"🆔 ID: (\d+)", original_text)
            
            if match:
                user_id = int(match.group(1))
                # Отправляем копию ответа админа пользователю
                await message.copy_to(user_id, caption=f"Ответ поддержки:\n\n{message.text or message.caption or ''}")
            else:
                # Опционально: сообщаем админу, что ID не найден
                pass