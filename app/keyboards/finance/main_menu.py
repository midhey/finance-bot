from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def main_finance_keyboard() -> InlineKeyboardMarkup:
    """
    Главное финансовое меню для пользователя, который уже в группе:
      ➖ Расход    ➕ Доход
      💼 Кошельки  📊 Статистика
      ⚙️ Настройки группы
    """
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="➖ Расход", callback_data="finance:expense"),
        InlineKeyboardButton(text="➕ Доход", callback_data="finance:income"),
    )
    builder.row(
        InlineKeyboardButton(text="💼 Кошельки", callback_data="finance:wallets"),
        InlineKeyboardButton(text="📊 Статистика", callback_data="finance:stats"),
    )
    builder.row(
        InlineKeyboardButton(text="⚙️ Настройки группы", callback_data="group:settings")
    )
    return builder.as_markup()
