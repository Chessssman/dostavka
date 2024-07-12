from aiogram import Router, types
from aiogram.types import CallbackQuery
from keyboard import get_start_keyboard  # Импортируйте другие необходимые функции
from keyboard import get_app_keyboard

# Создаем роутер для callback query
callback_router = Router()

@callback_router.callback_query()
async def process_callback(callback: CallbackQuery):
    if callback.data == "get_product":
        await callback.message.answer(
    "Чтобы начать пользоваться бесплатной доставкой, скачайте <b>приложение</b>.\n"
    "<a href='https://apps.apple.com/us/app/%D0%BE%D0%B7%D0%BE%D0%BD-%D0%BE%D0%BD%D0%BB%D0%B0%D0%B9%D0%BD-%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D0%BD%D0%B5%D1%82-%D0%BC%D0%B0%D0%B3%D0%B0%D0%B7%D0%B8%D0%BD/id407804998'>App Store</a>\n"
    "<a href='https://play.google.com/store/apps/details?id=ru.ozon.app.android'>Google Play</a>\n"
    "<a href='https://appgallery.huawei.com/#/app/C100847609'>AppGallery</a>\n"
    "<a href='https://apps.rustore.ru/app/ru.ozon.app.android'>RuStore</a>\n",
    parse_mode="HTML",
    reply_markup= get_app_keyboard()
)

    elif callback.data == "info":
        await callback.message.answer(
            "Подробную информацию о нашем сервисе можно найти <a href='https://example.com/info'>здесь</a>.",
            parse_mode="HTML"
        )
    elif callback.data == "support":
        await callback.message.answer(
            "Свяжитесь с нашей <a href='https://t.me/support_channel'>службой поддержки</a>.",
            parse_mode="HTML"
        )
    else:
        await callback.answer("Неизвестная команда")
    
    # Не забудьте ответить на callback query, чтобы убрать "часики" на кнопке
    await callback.answer()