from app.models.group import Group
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession


class GroupRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, name) -> Group:
        group = Group(name=name)
        self.session.add(group)
        await self.session.flush()
        return group

    async def get_by_id(self, id) -> Group | None:
        result = await self.session.execute(select(Group).where(Group.id == id))
        return result.scalar_one_or_none()

    async def update_name(self, id, name) -> bool:
        result = await self.session.execute(
            update(Group).where(Group.id == id).values(name=name)
        )
        return result.rowcount > 0

    async def delete(self, id) -> bool:
        result = await self.session.execute(delete(Group).where(Group.id == id))
        return result.rowcount > 0
