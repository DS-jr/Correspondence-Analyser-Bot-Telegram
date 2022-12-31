import json
from sqlalchemy import create_engine
from sqlalchemy.sql import text

import config

engine = create_engine(config.DATABASE_STRING, future=True)

with open("result.json") as f:
    data = json.load(f)

with engine.connect() as con:

    for chat in data["chats"]["list"]:
        statement = text(
            """
            INSERT INTO telegram_chat(telegram_id, name, type) 
            VALUES(:id, :name, :type)
            ON CONFLICT (telegram_id) DO NOTHING 
            """
        )
        con.execute(
            statement,
            {"id": chat["id"], "name": chat.get("name"), "type": chat["type"]},
        )

        for message in chat["messages"]:
            statement = text(
                """
                INSERT INTO telegram_message(telegram_id, date, unix_timestamp, from_name, from_id, chat_id) 
                VALUES(:id, :date, :unix_timestamp, :from_name, :from_id, :chat_id)
                ON CONFLICT (telegram_id) DO NOTHING 
                """
            )
            con.execute(
                statement,
                {
                    "id": message["id"],
                    "date": message["date"],
                    "unix_timestamp": message["date_unixtime"],
                    "from_name": message.get("from"),
                    "from_id": message.get("from_id"),
                    "chat_id": chat["id"],
                },
            )

        con.commit()
