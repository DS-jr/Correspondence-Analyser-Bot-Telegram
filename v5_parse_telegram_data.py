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

# Proceed from here!
        # for message in chat["messages"]:
        #     var_2 = text( ..??..
        #     )

    con_5.commit()




        # print(chat["type"])
    # print(type(exported_data_dict["chats"]["list"]))
    # ...??...

    # (?) Try to delete 'text' module: is it vital here?

    # (?!) Test what happens if I do NOT use colons in "VALUES" line







