import json, config, dateutil.parser
from sqlalchemy import create_engine, insert, delete
from sqlalchemy.sql import text
from create_tables_in_DB import TelegramChat, TelegramMessage

with open("export_result_TG_account_N4.json") as json_file:
    exported_data_dict = json.load(json_file)
    # print(type(exported_data_dict))

engine = create_engine(config.DATABASE_STRING, future=True)  # Engine is a factory that can create new database connections

# Insert chat data (telegram_id, name, type) into SQLite:

# ins = students.insert().values(name = 'Ravi', lastname = 'Kapoor')   # (CDL) Example
# conn = engine.connect()
# result = conn.execute(ins)

with engine.connect() as con_5:

    delete_all = delete(TelegramChat)    # (CDL) For testing purposes
    con_5.execute(delete_all)

    for chat in exported_data_dict["chats"]["list"]:
        insert_5 = insert(TelegramChat).values(telegram_id=chat["id"], name=chat.get("name"), type=chat["type"])
        result_5 = con_5.execute(insert_5)

        for message in chat["messages"]:
            insert_51 = insert(TelegramMessage).values(telegram_id=message["id"], date=dateutil.parser.parse(message["date"]), unix_timestamp=message["date_unixtime"], from_name=message.get("from"), from_id=message.get("from_id"), chat_id=chat["id"]) # (?) (error: NOT NULL constraint failed: telegram_message.id ) (hypothesis) Auto-increment is NOT working in "id" column
#            insert_51 = insert(TelegramMessage).values(id=message["id"], telegram_id=message["id"], date=dateutil.parser.parse(message["date"]), unix_timestamp=message["date_unixtime"], from_name=message.get("from"), from_id=message.get("from_id"), chat_id=chat["id"]) # This "crutch" experimental draft variant worked w/ NO errors
            result_51 = con_5.execute(insert_51)

#        id = chat.["id"]  # did NOT work
#        id = chat.get("id")  # did NOT work
#        telegram_id = message["id"]  # Old variant that did NOT work


        # date = message["date"]
        # telegram_id, date, unix_timestamp, from_name, from_id, chat_id
        #             con_5.execute(var_2, {"id": message["id"], "date": message["date"], "unix_timestamp": message["date_unixtime"], "from_name": message.get("from"), "from_id": message.get("from_id"), "chat_id": chat["id"]},)
        # for message in chat["messages"]:



        # insert_5 = TelegramChat().insert().values(telegram_id = chat["id"], name = chat.get("name"), type = chat["type"])

        # for chat in exported_data_dict["chats"]["list"]:
#         var_1 = text(
#             """
#             INSERT INTO telegram_chat (telegram_id, name, type)
#             VALUES(:id, :name, :type)
#             ON CONFLICT (telegram_id) DO NOTHING
#             """
#         )
#         con_5.execute(var_1, {"id": chat["id"], "name": chat.get("name"), "type": chat["type"]},)   # "id" or "telegram_id" should be used?
#
#         for message in chat["messages"]:
#             var_2 = text(
#                 """
#                 INSERT INTO telegram_message (telegram_id, date, unix_timestamp, from_name, from_id, chat_id)
#                 VALUES(:id, :date, :unix_timestamp, :from_name, :from_id, :chat_id)
#                 ON CONFLICT (telegram_id) DO NOTHING
#                 """
#             )
#             # if message["id"] is None:
#             #     print("id is None!")
#             #     raise Exception
#             con_5.execute(var_2, {"id": message["id"], "date": message["date"], "unix_timestamp": message["date_unixtime"], "from_name": message.get("from"), "from_id": message.get("from_id"), "chat_id": chat["id"]},)
#             # (?) Can "chat_id_2: chat["id"]" be used in the previous line? Or is it 'duplicating'? (if yes - how to do that correctly?
#
        con_5.commit()



        # print(chat["type"])
    # print(type(exported_data_dict["chats"]["list"]))
    # ...??...

    # (?) Try to delete 'text' module: is it vital here?

    # (?!) Test what happens if I do NOT use colons in "VALUES" line







