import asyncio
import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.exceptions import TelegramAPIError
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_start_keyboard():
    buttons = [
        [InlineKeyboardButton(text="📦 Как пользоваться доставкой?", callback_data="get_product")],
        [InlineKeyboardButton(text="ℹ️ Как платить?", callback_data="info")],
        [InlineKeyboardButton(text="📍  Найти пункт выдачи поблизости", callback_data="support")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard