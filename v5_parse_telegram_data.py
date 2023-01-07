import json, config
from sqlalchemy import create_engine
from sqlalchemy.sql import text

with open("export_result_TG_account_N4.json") as json_file:
    exported_data_dict = json.load(json_file)
    # print(type(exported_data_dict))

engine = create_engine(config.DATABASE_STRING, future=True)  # Engine is a factory that can create new database connections

# insert chat data (telegram_id, name, type) into SQLite:
with engine.connect() as con_5:

    for chat in exported_data_dict["chats"]["list"]:
        var_1 = text(
        """
        INSERT INTO telegram_chat (telegram_id, name, type) 
        VALUES(:id_1, :name_1, :type_1)   
        ON CONFLICT (telegram_id) DO NOTHING
        """
        )
        con_5.execute(var_1, {"id_1": chat["id"], "name_1": chat.get("name"), "type_1": chat["type"]},)

        for message in chat["messages"]:
            var_2 = text(
            """
            INSERT INTO telegram_message (telegram_id, date, unix_timestamp, from_name, from_id, chat_id)
            VALUES(:id_2, :date_2, :unix_timestamp_2, :from_name_2, :from_id_2, :chat_id_2) 
            ON CONFLICT(telegram_id) DO NOTHING
            """
            )
            con_5.execute(var_2, {"id_2": message["id"], "date_2": message["date"], "unix_timestamp_2": message["date_unixtime"], "from_name_2": message.get("from"), "from_id_2": message.get("from_id"), "chat_id_2": chat["id"]},)
            # Can "chat_id_2: chat["id"]" be used in the previous line? Or is it 'duplicating'? (if yes - how to do that correctly?

        con_5.commit()



        # print(chat["type"])
    # print(type(exported_data_dict["chats"]["list"]))
    # ...??...

    # (?) Try to delete 'text' module: is it vital here?

    # (?!) Test what happens if I do NOT use colons in "VALUES" line







