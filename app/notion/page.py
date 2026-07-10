from app.notion.client import notion


def create_page(database_id: str, properties: dict, icon: str | None = None):
    """
    Erstellt einen Eintrag in einer Notion-Datenbank.
    """

    body = {
        "parent": {
            "type": "data_source_id",
            "data_source_id": database_id
        },
        "properties": properties
    }

    if icon:
        body["icon"] = {
            "type": "emoji",
            "emoji": icon
        }

    return notion.pages.create(**body)