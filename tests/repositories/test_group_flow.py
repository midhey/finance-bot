import pytest
from app.db import async_session
from app.repositories.group import GroupRepository
from app.repositories.group_user import GroupUserRepository


@pytest.mark.asyncio
async def test_group_and_user_link_crud():
    async with async_session() as session:
        group_repo = GroupRepository(session)
        group_user_repo = GroupUserRepository(session)

        # 1. Создание группы
        group = await group_repo.create("Test Group")
        await session.commit()
        assert group.id is not None

        # 2. Привязка пользователя
        user_id = 99999
        await group_user_repo.add_user(user_id=user_id, group_id=group.id)
        await session.commit()

        group_id = await group_user_repo.get_user_group(user_id)
        assert group_id == group.id

        # 3. Переименование группы
        updated = await group_repo.update_name(group.id, "Updated Group")
        await session.commit()
        assert updated is True

        reloaded = await group_repo.get_by_id(group.id)
        assert reloaded.name == "Updated Group"

        # 4. Удаление пользователя из группы
        removed = await group_user_repo.remove_user(user_id)
        await session.commit()
        assert removed is True
        assert await group_user_repo.get_user_group(user_id) is None

        # 5. Удаление самой группы
        deleted = await group_repo.delete(group.id)
        await session.commit()
        assert deleted is True
        assert await group_repo.get_by_id(group.id) is None
