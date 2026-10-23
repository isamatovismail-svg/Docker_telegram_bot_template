from aiogram.fsm.state import State, StatesGroup


class UserFormState(StatesGroup):
    """
    So'rovnoma (FSM) holatlari:
      name     -> foydalanuvchi ismini kiritadi
      age      -> yoshini kiritadi
      feedback -> fikr-mulohaza kiritadi
    """
    name     = State()
    age      = State()
    feedback = State()
