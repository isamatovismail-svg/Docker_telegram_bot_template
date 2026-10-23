from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message(F.text == "ℹ️ Ma'lumot")
async def info_handler(message: Message) -> None:
    await message.answer(
        "ℹ️ <b>Loyiha haqida:</b>\n\n"
        "Bu shablon <b>Aiogram 3.x</b>, <b>SQLite</b> va <b>Docker</b> "
        "asosida yozilgan bo'lib, yangi bot loyihalaringiz uchun tayyor asos hisoblanadi."
    )


@router.message(F.text == "📞 Aloqa")
async def contact_handler(message: Message) -> None:
    await message.answer(
        "📞 <b>Aloqa:</b>\n\n"
        "Savollar uchun murojaat qiling: @your_username"
    )


@router.message(F.text)
async def echo_handler(message: Message) -> None:
    """
    Boshqa barcha matnli xabarlarga echo javob qaytaradi.
    """
    await message.answer(f"📩 Siz yubordingiz:\n<i>{message.text}</i>")
