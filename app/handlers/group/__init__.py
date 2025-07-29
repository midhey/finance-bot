from aiogram import Router
from .commands import router as commands_router
from .callbacks import router as callbacks_router

group_router = Router()
group_router.include_router(commands_router)
group_router.include_router(callbacks_router)

__all__ = ["group_router"]
