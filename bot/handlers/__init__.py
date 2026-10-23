from aiogram import Router

from .start import router as start_router
from .form  import router as form_router
from .admin import router as admin_router
from .echo  import router as echo_router

# Asosiy router — barcha ichki routerlarni o'z ichiga oladi.
# Tartib muhim: echo eng oxirida bo'lishi kerak (fallback).
router = Router()
router.include_router(start_router)
router.include_router(form_router)
router.include_router(admin_router)
router.include_router(echo_router)

__all__ = ["router"]
