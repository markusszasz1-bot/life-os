from app.notion.client import notion


def find_database(name: str):
    """
    Sucht nach einer Datenbank anhand ihres Namens.
    """

    response = notion.search(
        query=name,
        filter={
            "property": "object",
            "value": "data_source"
        }
    )

    for result in response["results"]:

        title = result.get("title", [])

        if title and title[0]["plain_text"] == name:
            return result

    return None