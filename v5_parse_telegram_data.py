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
        var_1 = text(  # (?) Try to delete 'text' module: is it vital here?
        # (?!) Test what happens if I do NOT use colons in line 18
        """
        INSERT INTO telegram_chats (name, type, telegram_id,) 
        VALUES(:name_1, :type_1, :id_1)   
        ON CONFLICT (telegram_id) DO NOTHING
        """
        )
        con_5.execute(var_1, {"id_1": chat["id"], "name_1": chat["name"], "type_1": chat["type"]})

        for message in chat["messages"]:
            var_2 = text(
            # Proceed from here!
            )




        # print(chat["type"])
    # print(type(exported_data_dict["chats"]["list"]))
    # ...??...

