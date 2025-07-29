from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from app.models.group import Group


def group_settings_keyboard(groups: list[Group]) -> InlineKeyboardMarkup:
    """
    Список групп без кнопок создания/входа.
    Показывается в разделе "Настройки группы".
    """
    builder = InlineKeyboardBuilder()
    for group in groups:
        builder.row(
            InlineKeyboardButton(
                text=group.name, callback_data=f"group:select:{group.id}"
            )
        )
    return builder.as_markup()


def group_action_keyboard(group: Group) -> InlineKeyboardMarkup:
    """
    Меню действий для конкретной группы:
    """
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text="📨 Пригласить", callback_data=f"group:invite:{group.id}"
        )
    )
    builder.row(
        InlineKeyboardButton(
            text="🚪 Покинуть группу", callback_data=f"group:leave:{group.id}"
        )
    )
    return builder.as_markup()
