from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.keyboards.default import main_menu_keyboard, cancel_keyboard
from bot.states.user_state import UserFormState

router = Router()


# ------------------------------------------------------------------
# Bekor qilish (istalgan holatda)
# ------------------------------------------------------------------
@router.message(Command("cancel"))
@router.message(F.text == "❌ Bekor qilish")
async def cmd_cancel(message: Message, state: FSMContext) -> None:
    current = await state.get_state()
    if current is None:
        await message.answer("Hech qanday faol amaliyot yo'q.", reply_markup=main_menu_keyboard())
        return
    await state.clear()
    await message.answer("❌ So'rovnoma bekor qilindi.", reply_markup=main_menu_keyboard())


# ------------------------------------------------------------------
# So'rovnomani boshlash
# ------------------------------------------------------------------
@router.message(F.text == "📝 So'rovnoma")
@router.message(Command("form"))
async def start_form(message: Message, state: FSMContext) -> None:
    await state.set_state(UserFormState.name)
    await message.answer(
        "📝 <b>So'rovnoma boshlandi!</b>\n\n"
        "Ismingizni kiriting:",
        reply_markup=cancel_keyboard()
    )


# ------------------------------------------------------------------
# 1-qadam: Ism
# ------------------------------------------------------------------
@router.message(UserFormState.name, F.text)
async def step_name(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    await state.set_state(UserFormState.age)
    await message.answer(
        f"Rahmat, <b>{message.text}</b>! 😊\n\n"
        "Yoshingizni kiriting <i>(faqat raqam)</i>:",
        reply_markup=cancel_keyboard()
    )


# ------------------------------------------------------------------
# 2-qadam: Yosh
# ------------------------------------------------------------------
@router.message(UserFormState.age, F.text)
async def step_age(message: Message, state: FSMContext) -> None:
    if not message.text.isdigit():
        await message.answer("⚠️ Iltimos, faqat raqam kiriting (masalan: <b>25</b>):")
        return

    await state.update_data(age=int(message.text))
    await state.set_state(UserFormState.feedback)
    await message.answer(
        "Bot bo'yicha fikr yoki taklifingizni yozing:",
        reply_markup=cancel_keyboard()
    )


# ------------------------------------------------------------------
# 3-qadam: Fikr → Xulosa
# ------------------------------------------------------------------
@router.message(UserFormState.feedback, F.text)
async def step_feedback(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    await state.clear()

    await message.answer(
        "✅ <b>So'rovnoma yakunlandi!</b>\n\n"
        f"👤 <b>Ism:</b>  {data['name']}\n"
        f"🎂 <b>Yosh:</b> {data['age']}\n"
        f"💬 <b>Fikr:</b> {message.text}",
        reply_markup=main_menu_keyboard()
    )
