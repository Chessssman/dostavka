from aiogram import Router, types
from aiogram.types import CallbackQuery
from keyboard import get_start_keyboard  # Импортируйте другие необходимые функции
from keyboard import get_app_keyboard
from keyboard import get_pay_keyboard

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
            "Выберите ваш способ оплаты:",
            parse_mode="HTML",
            reply_markup= get_pay_keyboard()
        )
    

    elif callback.data == "set_bank_card":
        await callback.message.answer(
            "<b>💸Привязать банковскую карту</b>\n" 
            "1. При оформлении заказа в разделе <b>Способ оплаты</b> выберите <b>Новой картой</b> и нажмите <b>Оплатить онлайн</b>.\n"
            "2. В открывшемся окне введите номер карты, срок действия карты и CVV/CVC код.\n" 
            "3. Нажмите розовую кнопку <b>Оплатить</b>.\n" 
            "4. Сохраните этот способ оплаты.\n",
            parse_mode="HTML"
        )
    
    elif callback.data == "set_sbp_card":
        await callback.message.answer(
            "<b>💸СБП</b>\n" 
            "1. При оформлении заказа в разделе <b>Способ оплаты</b> выберите <b>Система быстрых платежей</b> и нажмите <b>Оплатить онлайн</b>.\n"
            "2. Откройте мобильное приложение вашего банка и перейдите в раздел <b>Платежи</b> выберите <b>Оплатить по QR-коду</b>.\n" 
            "3. Отсканируйте QR-код и подтвердите оплату.\n" 
            "4. Сохраните этот способ оплаты.\n",
            parse_mode="HTML"
        )

    elif callback.data  == "set_ozon_bank_card":
        await callback.message.answer(
            "<b>💸Ozon Bank</b>\n" 
            "1. При оформлении заказа в разделе <b>Способ оплаты</b> выберите <b>Ozon карту</b> и нажмите <b>Оплатить онлайн</b>.\n"
            "2. Введите 4-х значный пароль от карты Ozon и нажмите <b>Оплатить онлайн</b>.\n"  
            "4. Сохраните этот способ оплаты.\n",
            parse_mode="HTML"
        )
    
    else:
        await callback.answer("Неизвестная команда")
    
    # Не забудьте ответить на callback query, чтобы убрать "часики" на кнопке
    await callback.answer()