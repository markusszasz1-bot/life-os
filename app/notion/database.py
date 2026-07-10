from app.notion.client import notion, PARENT_PAGE_ID
from app.notion.search import find_database


def create_database(name: str, properties: dict):
    """
    Erstellt eine Notion-Datenbank, falls sie noch nicht existiert.
    """

    # Prüfen, ob die Datenbank bereits existiert
    existing = find_database(name)

    if existing:
        print(f"✅ Datenbank '{name}' existiert bereits.")
        return existing

    print(f"📦 Erstelle Datenbank '{name}'...")

    response = notion.databases.create(
        parent={
            "type": "page_id",
            "page_id": PARENT_PAGE_ID,
        },
        title=[
            {
                "type": "text",
                "text": {
                    "content": name
                }
            }
        ],
        properties=properties,
    )

    print(f"✅ Datenbank '{name}' erfolgreich erstellt.")

    return response