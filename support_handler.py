# support_handler

from aiogram import Router, types, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import re

class SupportState(StatesGroup):
    waiting_for_question = State()

callback_router = Router()

@callback_router.callback_query(lambda c: c.data == "support")
async def support_start(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("🛠 Опишите вашу проблему (можно фото/видео).")
    await state.set_state(SupportState.waiting_for_question)

@callback_router.message(SupportState.waiting_for_question)
async def receive_support_question(message: types.Message, state: FSMContext):
    support_chat_id = -1002296401929 
    
    user_id = message.from_user.id
    text_content = message.text or message.caption or "[Файл]"
    
    # !!! ВАЖНО: Добавляем ID в начало сообщения !!!
    info_header = f"ID: {user_id}\nВопрос от пользователя:\n"
    
    full_text = info_header + text_content

    # Используем copy_to, чтобы работали вложения
    await message.copy_to(support_chat_id, caption=full_text)

    await message.answer("Ваш вопрос отправлен.")
    await state.clear()


# Обработчик ответа (парсим ID из строки "ID: 12345")
@callback_router.message()
async def forward_support_response(message: types.Message):
    if message.chat.id == -1002296401929: # ID чата поддержки
        # Проверяем, есть ли реплай с ID
        if message.reply_to_message:
            original_text = message.reply_to_message.text or message.reply_to_message.caption or ""
            match = re.search(r"ID:\s*(\d+)", original_text)
            
            if match:
                user_id = int(match.group(1))
                await message.copy_to(user_id, caption=f"Ответ техподдержки:\n\n{message.text or message.caption or ''}")
                return

        # Если старая логика (через двоеточие в самом сообщении "12345: ответ"), оставляем как запасной вариант:
        text = message.text or message.caption or ""
        parts = text.split(":", 1)
        if len(parts) == 2 and parts[0].strip().isdigit():
            user_id = int(parts[0])
            answer_text = parts[1].strip()
            await message.bot.send_message(user_id, f"Ответ техподдержки:\n\n{answer_text}")