from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from models.talent import Talent
from states.example import ExampleState
from utils.notion.create_talent import write_in_db

reply_message_router = Router(name=__name__)


@reply_message_router.message()
async def reply_message(message: Message, state: FSMContext):
    if message.forward_sender_name is not None or message.forward_from is not None:
        telegram_id = 404
        username = ""
        print("Here's forward message")
        if message.forward_from is not None:
            telegram_id = message.forward_from.id
            username = message.forward_from.username
        else:
            username = message.forward_sender_name
        talent = Talent(
            telegram_id=telegram_id,
            username=username,
            talent_description=message.text.replace("\n", " "),
        )
        print(talent)
        write_in_db(talent)
    else:
        print(f"Just a normal message {message}")
