from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


class SampleCallbackData(CallbackData, prefix="sample"):
    """
    Inline tugmalar uchun CallbackData fabrikasi.
    """
    action:  str
    item_id: int


def get_sample_inline_keyboard() -> InlineKeyboardMarkup:
    """
    Namunaviy Inline klaviatura:
      - 👍 Ma'qul    (callback)
      - 👎 Rad etish (callback)
      - 🌐 Sayt      (URL tugma)
    """
    builder = InlineKeyboardBuilder()

    builder.button(
        text="👍 Ma'qul",
        callback_data=SampleCallbackData(action="like", item_id=1).pack()
    )
    builder.button(
        text="👎 Rad etish",
        callback_data=SampleCallbackData(action="dislike", item_id=1).pack()
    )
    builder.button(
        text="🌐 python.org",
        url="https://python.org"
    )
    # 1-qatorda 2 ta, 2-qatorda 1 ta
    builder.adjust(2, 1)

    return builder.as_markup()
