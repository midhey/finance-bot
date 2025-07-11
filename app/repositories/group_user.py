from app.models.group_user import GroupUser
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession


class GroupUserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_user(self, user_id, group_id) -> GroupUser:
        user = GroupUser(user_id=user_id, group_id=group_id)
        self.session.add(user)
        await self.session.flush()
        return user

    async def remove_user(self, user_id, group_id) -> bool:
        result = await self.session.execute(
            delete(GroupUser).where(
                GroupUser.user_id == user_id, GroupUser.group_id == group_id
            )
        )
        return result.rowcount > 0

    async def get_user_groups(self, user_id) -> list[int]:
        result = await self.session.execute(
            select(GroupUser.group_id).where(GroupUser.user_id == user_id)
        )
        return [row[0] for row in result.fetchall()]

    async def get_group_users(self, group_id) -> list[int]:
        result = await self.session.execute(
            select(GroupUser.user_id).where(GroupUser.group_id == group_id)
        )
        return [row[0] for row in result.fetchall()]
