import pytest
from app.general.state import state
from app.repositories.group import GroupRepository
from app.repositories.group_user import GroupUserRepository


@pytest.mark.asyncio
async def test_group_and_user_link_crud():
    async with state.db() as session:
        group_repo = GroupRepository(session)
        group_user_repo = GroupUserRepository(session)

        # 1. Создание группы
        group = await group_repo.create("Test Group")
        await session.commit()
        assert group.id is not None

        # 2. Привязка пользователя
        user_id = 99999
        link = await group_user_repo.add_user(user_id=user_id, group_id=group.id)
        await session.commit()
        assert link.id is not None

        # 3. Проверка привязки (get_user_groups)
        group_ids = await group_user_repo.get_user_groups(user_id)
        assert group.id in group_ids

        # 4. Проверка обратной связи (get_group_users)
        user_ids = await group_user_repo.get_group_users(group.id)
        assert user_id in user_ids

        # 5. Переименование группы
        updated = await group_repo.update_name(group.id, "Updated Group")
        await session.commit()
        assert updated is True

        reloaded = await group_repo.get_by_id(group.id)
        assert reloaded.name == "Updated Group"

        # 6. Удаление пользователя из группы
        removed = await group_user_repo.remove_user(user_id, group.id)
        await session.commit()
        assert removed is True

        assert group.id not in await group_user_repo.get_user_groups(user_id)
        assert user_id not in await group_user_repo.get_group_users(group.id)

        # 7. Удаление самой группы
        deleted = await group_repo.delete(group.id)
        await session.commit()
        assert deleted is True
        assert await group_repo.get_by_id(group.id) is None
