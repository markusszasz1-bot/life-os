from app.seed.areas import AREAS
from app.notion.page import create_page


def seed_areas(database):

    database_id = database["id"]

    for area in AREAS:

        print(f"➕ {area['name']}")

        create_page(
            database_id,
            properties={
                "Name": {
                    "title": [
                        {
                            "text": {
                                "content": area["name"]
                            }
                        }
                    ]
                },
                "Icon": {
                    "rich_text": [
                        {
                            "text": {
                                "content": area["icon"]
                            }
                        }
                    ]
                },
                "Order": {
                    "number": area["order"]
                },
                "Active": {
                    "checkbox": True
                }
            },
            icon=area["icon"]
        )