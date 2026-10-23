from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def main_menu_keyboard() -> ReplyKeyboardMarkup:
    """
    Asosiy menyu: Reply klaviatura.
    Chiqish: 2 tugma 1-qatorda, 1 tugma 2-qatorda.
    """
    builder = ReplyKeyboardBuilder()
    builder.button(text="ℹ️ Ma'lumot")
    builder.button(text="📝 So'rovnoma")
    builder.button(text="📞 Aloqa")
    builder.adjust(2, 1)

    return builder.as_markup(
        resize_keyboard=True,
        input_field_placeholder="Bo'limni tanlang..."
    )


def cancel_keyboard() -> ReplyKeyboardMarkup:
    """
    So'rovnoma davomida bekor qilish uchun klaviatura.
    """
    builder = ReplyKeyboardBuilder()
    builder.button(text="❌ Bekor qilish")

    return builder.as_markup(resize_keyboard=True)
