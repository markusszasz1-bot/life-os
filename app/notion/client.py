from notion_client import Client
from dotenv import load_dotenv
import os

load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
PARENT_PAGE_ID = os.getenv("NOTION_PARENT_PAGE_ID")

if not NOTION_TOKEN:
    raise Exception("NOTION_TOKEN fehlt.")

if not PARENT_PAGE_ID:
    raise Exception("NOTION_PARENT_PAGE_ID fehlt.")

notion = Client(auth=NOTION_TOKEN)