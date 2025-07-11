from app.repositories.group import GroupRepository
from app.repositories.group_user import GroupUserRepository
from app.general.state import state
from app.models.group import Group
import secrets


class GroupService:
    def __init__(self, session):
        self.session = session
        self.group_repository = GroupRepository(session)
        self.group_user_repository = GroupUserRepository(session)

    async def create_group(self, user_id, group_name) -> Group:
        group = await self.group_repository.create(group_name)
        await self.group_user_repository.add_user(user_id, group.id)
        return group

    async def leave_group(self, user_id, group_id) -> bool:
        return await self.group_user_repository.remove_user(user_id, group_id)

    async def rename_group(self, group_id, new_name) -> bool:
        return await self.group_repository.update_name(group_id, new_name)

    async def delete_group(self, group_id) -> bool:
        users = await self.group_user_repository.get_group_users(group_id)
        for user_id in users:
            await self.group_user_repository.remove_user(user_id, group_id)
        return await self.group_repository.delete(group_id)

    async def generate_invite(self, group_id) -> str:
        code = secrets.token_hex(4).upper()[:6]
        await state.redis.set(f"invite:{code}", group_id, ex=900)
        return code

    async def join_by_invite(self, user_id, code) -> bool:
        group_id = await state.redis.get(f"invite:{code}")
        if group_id is not None:
            if int(group_id) in await self.get_user_groups(user_id):
                return False
            await self.group_user_repository.add_user(user_id, int(group_id))
            await state.redis.delete(f"invite:{code}")
            return True
        return False

    async def get_user_groups(self, user_id) -> list[int]:
        return await self.group_user_repository.get_user_groups(user_id)

    async def get_group_users(self, group_id) -> list[int]:
        return await self.group_user_repository.get_group_users(group_id)
