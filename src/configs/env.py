import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
NOTION_TOKEN = os.getenv("NOTION_API_KEY")
PAGE_ID = os.getenv("PAGE_ID")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")