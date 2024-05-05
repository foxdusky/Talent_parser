from notion_client import Client
from configs.env import NOTION_TOKEN, PAGE_ID, NOTION_DATABASE_ID
from models.talent import Talent


def get_pages(client: Client):
    return client.pages.retrieve(PAGE_ID)


def read_in_db():
    client = authorization()
    db_data = client.databases.retrieve(database_id=NOTION_DATABASE_ID)
    print(type(db_data))
    print(db_data)


def authorization() -> Client:
    return Client(auth=NOTION_TOKEN)


def write_in_db(talent: Talent):
    client = authorization()
    client.pages.create(
        **{
            "parent": {
                "database_id": NOTION_DATABASE_ID
            },
            "properties": {
                "Telegram ID": {
                    "type": "title",
                    "title": [
                        {
                            "type": "text",
                            "text": {"content": str(talent.telegram_id)}
                        }
                    ]
                },
                "Telegram Username": {
                    "type": "rich_text",
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {"content": talent.username}
                        }
                    ]
                },
                "User Talent Description": {
                    "type": "rich_text",
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {"content": talent.talent_description}
                        }
                    ]
                }
            }
        }
    )
