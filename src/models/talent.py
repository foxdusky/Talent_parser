from pydantic import BaseModel


class Talent(BaseModel):
    telegram_id: int
    username: str
    talent_description: str
