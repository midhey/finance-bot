from aiogram import Router
from aiogram.filters.command import Command
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.group import GroupService
from app.keyboards.group import main_menu_keyboard, user_groups_keyboard

router = Router()


@router.message(Command("start"))
async def cmd_start(
    message: Message,
    session: AsyncSession,
):
    service = GroupService(session)
    user_id = message.from_user.id
    groups = await service.get_user_group_objects(user_id)

    if not groups:
        await message.answer(
            "Добро пожаловать! У вас ещё нет групп.\n"
            "Создайте новую или войдите по коду:",
            reply_markup=main_menu_keyboard(),
        )
    else:
        await message.answer(
            "Выберите одну из ваших групп:",
            reply_markup=user_groups_keyboard(groups),
        )
