from app.notion.database import create_database


def create_areas_database():

    return create_database(
        name="Areas",
        properties={
            "Name": {
                "title": {}
            },
            "Icon": {
                "rich_text": {}
            },
            "Order": {
                "number": {
                    "format": "number"
                }
            },
            "Active": {
                "checkbox": {}
            }
        }
    )