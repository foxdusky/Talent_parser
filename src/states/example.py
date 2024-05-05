from aiogram.fsm.state import StatesGroup, State


class ExampleState(StatesGroup):
    example = State()
    no_user_name = State()
