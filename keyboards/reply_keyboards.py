from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import ADMIN_ID


def get_main_keyboard(is_admin: bool = False):
    """Возвращает основную клавиатуру"""

    # Основные кнопки для всех пользователей
    buttons = [
        [KeyboardButton(text="🍽 Меню")],
        [KeyboardButton(text="💼 Бизнес-ланчи")],
        [KeyboardButton(text="🛒 Корзина"), KeyboardButton(text="📋 Мои заказы")],
        [KeyboardButton(text="⭐ Оставить отзыв"), KeyboardButton(text="ℹ О нас")]
    ]

    # Добавляем админские кнопки, если пользователь - Антон
    if is_admin:
        admin_buttons = [
            [KeyboardButton(text="📤 Загрузить меню")],
            [KeyboardButton(text="👥 Черный список"), KeyboardButton(text="✅ Выдать заказ")]
        ]
        buttons.extend(admin_buttons)

    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)


# Клавиатура для отмены действий
def get_cancel_keyboard():
    """Клавиатура с кнопкой отмены"""
    buttons = [[KeyboardButton(text="❌ Отмена")]]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)