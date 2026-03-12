from aiogram import Router, types
from aiogram.filters import Command
from datetime import datetime
from utils import json_worker
from utils.models import User
from keyboards.reply_keyboards import get_main_keyboard
from config import ADMIN_ID

router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    """Обработчик команды /start"""
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name

    # Проверяем, существует ли пользователь в базе
    existing_user = json_worker.get_user(user_id)

    if not existing_user:
        # Создаем нового пользователя
        new_user = User(
            user_id=user_id,
            username=username,
            first_name=first_name
        )
        json_worker.save_user(new_user.to_dict())

        # Приветственное сообщение для нового пользователя
        welcome_text = (
            f"👋 Привет, {first_name}!\n\n"
            f"Добро пожаловать в бот столовой Антона! 🍽\n\n"
            f"Здесь ты можешь:\n"
            f"• Посмотреть меню на сегодня\n"
            f"• Выбрать бизнес-ланч\n"
            f"• Сделать предзаказ\n"
            f"• Оставить отзыв\n\n"
            f"Используй кнопки меню для навигации 👇"
        )
    else:
        # Приветствие для существующего пользователя
        welcome_text = (
            f"С возвращением, {first_name}! 👋\n\n"
            f"Рады снова видеть тебя в нашей столовой!\n"
            f"Что будешь заказывать сегодня?"
        )

    # Проверяем, не в черном ли списке пользователь
    if json_worker.is_user_blacklisted(user_id):
        welcome_text += (
            f"\n\n⚠️ Внимание! Вы находитесь в черном списке из-за неявок.\n"
            f"Обратитесь к администратору для восстановления доступа."
        )

    # Отправляем приветствие с главной клавиатурой
    await message.answer(
        welcome_text,
        reply_markup=get_main_keyboard(is_admin=(user_id == ADMIN_ID))
    )


@router.message(Command("help"))
async def cmd_help(message: types.Message):
    """Обработчик команды /help"""
    help_text = (
        "🔍 Как пользоваться ботом:\n\n"
        "🍽 Меню - посмотреть все блюда\n"
        "💼 Бизнес-ланчи - готовые комплексы\n"
        "🛒 Корзина - просмотр и оформление заказа\n"
        "📋 Мои заказы - история и статусы\n"
        "⭐ Оставить отзыв - поделиться впечатлениями\n"
        "ℹ О нас - информация о столовой\n\n"
        "Если у вас возникли проблемы, обратитесь к администратору."
    )
    await message.answer(help_text)


@router.message(lambda message: message.text == "ℹ О нас")
async def about_us(message: types.Message):
    """Обработчик кнопки 'О нас'"""
    about_text = (
        "🏨 Столовая Антона\n\n"
        "📍 Адрес: ул. Примерная, д. 123\n"
        "⏰ Время работы: 9:00 - 18:00\n"
        "🍱 Горячее питание с 12:00 до 15:00\n\n"
        "Мы готовим для вас с любовью! ❤️\n"
        "Все блюда только из свежих продуктов.\n\n"
        "По вопросам сотрудничества: @anton_cafe"
    )
    await message.answer(about_text)


# Добавим простую проверку работы бота
@router.message(Command("ping"))
async def cmd_ping(message: types.Message):
    """Проверка работоспособности бота"""
    await message.answer("🏓 Pong! Бот работает!")