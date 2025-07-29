from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from app.models.group import Group


def main_menu_keyboard() -> InlineKeyboardMarkup:
    """
    Показываем, когда у пользователя НЕТ ни одной группы:
    """
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="➕ Создать группу", callback_data="group:create")
    )
    builder.row(
        InlineKeyboardButton(text="🔑 Войти в группу", callback_data="group:join")
    )
    return builder.as_markup()


def user_groups_keyboard(groups: list[Group]) -> InlineKeyboardMarkup:
    """
    Список групп пользователя + кнопки "Создать" и "Войти"
    """
    builder = InlineKeyboardBuilder()
    for group in groups:
        builder.row(
            InlineKeyboardButton(
                text=group.name, callback_data=f"group:select:{group.id}"
            )
        )
    builder.row(
        InlineKeyboardButton(text="➕ Создать новую", callback_data="group:create")
    )
    builder.row(
        InlineKeyboardButton(text="🔑 Войти по коду", callback_data="group:join")
    )
    return builder.as_markup()
