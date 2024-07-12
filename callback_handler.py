from aiogram import Router, types
from aiogram.types import CallbackQuery
from keyboard import get_start_keyboard  # Импортируйте другие необходимые функции

# Создаем роутер для callback query
callback_router = Router()

@callback_router.callback_query()
async def process_callback(callback: CallbackQuery):
    
    pass