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
    with open("data_info.json", "w") as f:
        pass
    pass


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
                    ]},
                "Telegram Username": {
                    "type": "rich_text",
                    "rich_text": [
                        {
                            "type": "rich_text",
                            "text": talent.username
                        }
                    ]
                },
                "User Talent Description": {
                    "type": "rich_text",
                    "rich_text": [
                        {
                            "type": "rich_text",
                            "text": talent.talent_description
                        }
                    ]
                },
                # "User Talent Description": {"type": "text", "text": talent.talent_description},
            }
        }
    )


if __name__ == "__main__":
    # print(get_pages(authorization()))
    tal = Talent(
        telegram_id=123523532,
        username="Fox",
        talent_description="Люблю суши"
    )
    write_in_db(tal)
    # read_in_db()
