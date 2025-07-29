from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.group import GroupService
from app.keyboards.finance import main_finance_keyboard

router = Router()


@router.callback_query(lambda c: c.data.startswith("group:select:"))
async def cb_select_group(
    query: CallbackQuery,
    state: FSMContext,
    session: AsyncSession,
):
    """
    Нажали на кнопку «<имя группы>»:
     – если уже в этой группе, шлём alert;
     – иначе сохраняем её и показываем финменю.
    """
    _, _, gid_str = query.data.partition("group:select:")
    group_id = int(gid_str)

    service = GroupService(session)
    group = await service.group_repository.get_by_id(group_id)

    data = await state.get_data()
    if data.get("current_group") == group_id:
        await query.answer(
            f"Вы уже находитесь в группе «{group.name}»", show_alert=True
        )
        return

    await state.update_data(current_group=group_id)

    await query.message.edit_text(
        f"Вы выбрали группу «{group.name}». Вот ваше финансовое меню:",
        reply_markup=main_finance_keyboard(),
    )
    await query.answer()
