def notice_schema(notice: dict) -> dict:
    return {
        "date": notice["date"],
        "title": notice["title"],
        "link": notice["link"] or ""
    }

def notices_list(notices: list) -> list:
    return [notice_schema(notice) for notice in notices]
