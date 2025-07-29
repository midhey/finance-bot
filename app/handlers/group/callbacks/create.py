from aiogram import Router
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.group import GroupService
from app.keyboards.group import user_groups_keyboard

router = Router()


class CreateGroupSG(StatesGroup):
    name = State()


@router.callback_query(lambda c: c.data == "group:create")
async def cb_start_create(query: CallbackQuery, state: FSMContext):
    """
    Пользователь нажал «Создать группу» — спрашиваем название.
    Переходим в состояние CreateGroupSG.name.
    """
    await query.message.answer("Введите название новой группы:")
    await state.set_state(CreateGroupSG.name)
    await query.answer()


@router.message(CreateGroupSG.name)
async def process_create_group(
    message: Message,
    state: FSMContext,
    session: AsyncSession,
):
    """
    Пользователь отправил имя группы —
    создаём её в БД через GroupService,
    выводим обновлённый список групп
    и сбрасываем FSM.
    """
    service = GroupService(session)
    name = message.text.strip()
    group = await service.create_group(message.from_user.id, name)

    groups = await service.get_user_group_objects(message.from_user.id)
    keyboard = user_groups_keyboard(groups)

    await message.answer(f"Группа «{group.name}» создана!", reply_markup=keyboard)
    await state.clear()
