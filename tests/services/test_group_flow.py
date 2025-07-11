import pytest
from app.general.state import state
from app.services.group import GroupService


@pytest.mark.asyncio
async def test_group_service_flow():
    user_id = 12345
    second_user_id = 67890

    async with state.db() as session:
        service = GroupService(session)

        # Создание группы
        group = await service.create_group(user_id, "My Family Budget")
        await session.commit()
        assert group.id is not None

        # Проверка участников
        users = await service.get_group_users(group.id)
        assert user_id in users

        # Переименование группы
        renamed = await service.rename_group(group.id, "Updated Budget")
        await session.commit()
        assert renamed is True

        # Генерация инвайта
        code = await service.generate_invite(group.id)
        assert code and len(code) == 6

        # Присоединение второго пользователя
        joined = await service.join_by_invite(second_user_id, code)
        await session.commit()
        assert joined is True

        # Повторное использование инвайта не сработает
        joined_again = await service.join_by_invite(second_user_id, code)
        assert joined_again is False

        # Выход пользователя
        left = await service.leave_group(second_user_id, group.id)
        await session.commit()
        assert left is True

        # Удаление группы
        deleted = await service.delete_group(group.id)
        await session.commit()
        assert deleted is True

        # Проверка, что группа удалена
        user_groups = await service.get_user_groups(user_id)
        assert group.id not in user_groups
