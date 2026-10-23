from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.config import config
from bot.database import get_user_count

router = Router()


@router.message(Command("admin"))
@router.message(Command("stats"))
async def admin_panel(message: Message) -> None:
    """
    /admin yoki /stats — bot statistikasini ko'rsatadi.
    Faqat ADMIN_IDS da ko'rsatilgan foydalanuvchilarga ruxsat beriladi.
    """
    user_id = message.from_user.id if message.from_user else 0

    # Agar ADMIN_IDS sozlangan bo'lsa, faqat adminlar kirishi mumkin
    if config.admin_ids and user_id not in config.admin_ids:
        await message.answer(
            "⛔ <b>Ruxsat yo'q!</b>\n"
            "Bu buyruq faqat bot administratorlari uchun."
        )
        return

    total_users = await get_user_count()

    await message.answer(
        "👑 <b>Admin Paneli</b>\n\n"
        f"👥 <b>Jami foydalanuvchilar:</b> {total_users} ta\n"
        f"🔑 <b>Adminlar soni:</b> {len(config.admin_ids)} ta"
    )
