from aiogram import Router

from .create import router as create_router
from .enter import router as enter_group_router
# from .join import router as join_router
# from .settings import router as settings_router

router = Router()
router.include_router(create_router)
router.include_router(enter_group_router)
# router.include_router(join_router)
# router.include_router(settings_router)

__all__ = ["router"]
