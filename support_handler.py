# support_handler

from aiogram import Router, types, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

# Состояния для машины состояний
class SupportState(StatesGroup):
    waiting_for_question = State()

callback_router = Router()

# Обработчик для кнопки "Обратиться в поддержку"
@callback_router.callback_query(lambda c: c.data == "support")
async def support_start(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("🛠 Пожалуйста, опишите вашу проблему или задайте вопрос (можно прикрепить фото/видео).")
    await state.set_state(SupportState.waiting_for_question)

# Обработчик получения вопроса
@callback_router.message(SupportState.waiting_for_question)
async def receive_support_question(message: types.Message, state: FSMContext):
    support_chat_id = -1002296401929 
    
    # Формируем заголовок с ID пользователя, чтобы админ знал, кому отвечать
    # Если вы используете логику "ответ реплаем", ID нужен в тексте
    header = f"{message.from_user.id}: Новый вопрос:\n"
    content = message.text or message.caption or ""
    
    full_text = header + content

    # Копируем сообщение админу
    await message.copy_to(support_chat_id, caption=full_text)

    await message.answer("Ваш вопрос был отправлен в техподдержку. Ожидайте ответа.")
    await state.clear()


# Обработчик пересылки ответа из техподдержки пользователю
# (Если используется формат ответа "ID: ответ")
@callback_router.message()
async def forward_support_response(message: types.Message):
    if message.chat.id == -1002296401929:
        # Получаем текст (или подпись, если админ отправил фото)
        admin_text = message.text or message.caption
        
        if admin_text and ":" in admin_text:
            parts = admin_text.split(":", 1)
            # Проверяем, что первая часть похожа на ID (цифры)
            if len(parts) == 2 and parts[0].strip().isdigit():
                user_id = int(parts[0])
                support_answer = parts[1].strip()
                
                # Отправляем ответ пользователю через copy_to (чтобы работали фото от админа)
                # Подменяем caption на чистый ответ (без ID)
                await message.copy_to(user_id, caption=f"Ответ от техподдержки:\n\n{support_answer}")
            else:
                # Если это не формат "ID: ответ", возможно это просто общение админов
                pass