import os
from datetime import date
from dotenv import load_dotenv
from notion_client import Client

load_dotenv()


def add_record(data: dict) -> str:
    client = Client(auth=os.environ["NOTION_TOKEN"])
    db_id = os.environ["NOTION_DB_ID"]

    properties = {
        "豆の種類": {
            "title": [{"text": {"content": data["bean"]}}]
        },
        "挽き目": {
            "number": data["grind"]
        },
        "豆の量(g)": {
            "number": data["bean_g"]
        },
        "水の量(ml)": {
            "number": data["water_ml"]
        },
        "抽出時間": {
            "rich_text": [{"text": {"content": data["brew_time"]}}]
        },
        "撹拌": {
            "checkbox": data["stir"]
        },
        "評価": {
            "number": data["rating"]
        },
        "記録日": {
            "date": {"start": date.today().isoformat()}
        },
    }

    if data["comment"]:
        properties["コメント"] = {
            "rich_text": [{"text": {"content": data["comment"]}}]
        }

    response = client.pages.create(
        parent={"database_id": db_id},
        properties=properties,
    )
    return response["url"]
