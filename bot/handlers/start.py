from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from bot.keyboards.default import main_menu_keyboard
from bot.keyboards.inline import get_sample_inline_keyboard, SampleCallbackData
from bot.database import add_user

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    """
    /start — botni ishga tushirish.
    Foydalanuvchini SQLite bazasiga avtomatik saqlaydi.
    """
    if message.from_user:
        await add_user(
            telegram_id=message.from_user.id,
            full_name=message.from_user.full_name,
            username=message.from_user.username,
        )

    name = message.from_user.full_name if message.from_user else "Foydalanuvchi"

    await message.answer(
        f"Assalomu alaykum, <b>{name}</b>! 👋\n\n"
        f"🤖 <b>Docker Telegram Bot</b> ga xush kelibsiz!\n"
        f"Ushbu bot <b>Aiogram 3.x</b>, <b>SQLite DB</b> va <b>Docker</b> asosida yozilgan.",
        reply_markup=main_menu_keyboard()
    )

    await message.answer(
        "Quyidagi inline tugmalardan birini sinab ko'ring:",
        reply_markup=get_sample_inline_keyboard()
    )


@router.message(Command("help"))
async def cmd_help(message: Message) -> None:
    """
    /help — mavjud buyruqlar ro'yxatini ko'rsatadi.
    """
    await message.answer(
        "📖 <b>Mavjud buyruqlar:</b>\n\n"
        "/start  — Botni qayta ishga tushirish\n"
        "/help   — Ushbu yordam oynasi\n"
        "/form   — So'rovnomani boshlash (FSM)\n"
        "/admin  — Admin statistikasi\n"
        "/cancel — Joriy amaliyotni bekor qilish"
    )


@router.callback_query(SampleCallbackData.filter())
async def handle_inline_callback(query: CallbackQuery, callback_data: SampleCallbackData) -> None:
    """
    Inline tugma bosilganda javob beradi.
    """
    if callback_data.action == "like":
        text = f"#{callback_data.item_id} ga 👍 Ma'qul bosdingiz!"
    else:
        text = f"#{callback_data.item_id} ga 👎 Rad etdingiz!"

    await query.answer(text=text, show_alert=True)
