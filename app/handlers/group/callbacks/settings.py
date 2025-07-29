from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.group import GroupService
from app.keyboards.group import group_action_keyboard

router = Router()


@router.callback_query(lambda callback: callback.data == "group:settings")
async def cb_group_settings(
    query: CallbackQuery, state: FSMContext, session: AsyncSession
):
    data = await state.get_data()
    group_id = data.get("current_group")

    if not group_id:
        await query.answer(
            "У вас нет активной группы. Выберите её прежде.", show_alert=True
        )
        return

    service = GroupService(session)
    group = await service.group_repository.get_by_id(group_id)

    await query.message.edit_text(
        f"Настройки группы «*{group.name}*»:",
        parse_mode="MarkdownV2",
        reply_markup=group_action_keyboard(group),
    )
    await query.answer()
