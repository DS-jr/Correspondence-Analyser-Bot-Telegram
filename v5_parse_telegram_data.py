import json, config, dateutil.parser
from sqlalchemy import create_engine, insert, delete, update, text
# from sqlalchemy.sql import text
from create_tables_in_DB import TelegramChat, TelegramMessage

with open("export_result_TG_account_N4.json") as json_file:
    exported_data_dict = json.load(json_file)
    # print(type(exported_data_dict))

engine = create_engine(
    config.DATABASE_STRING, future=True
)  # Engine is a factory that can create new database connections

with engine.connect() as con_5:
    # delete_all = delete(TelegramChat)    # (CDL) For testing purposes
    # con_5.execute(delete_all)

    for chat in exported_data_dict["chats"]["list"]:
        if not chat["messages"]:
            continue

        messages_min_date_confirmed = chat["messages"][0]["date"]

        insert_5 = insert(TelegramChat).values(
            telegram_id=chat["id"],
            name=chat.get("name"),
            type=chat["type"],
            first_date_from_the_left_side_in_messages_list=chat["messages"][0]["date"],
            # messages_min_date_checked=messages_min_date_confirmed,  # This line can be used if we prove: first_date_from_the_left_side_in_messages_list == messages_min_date_checked in ALL cases
        )  # (add?) dateutil.parser.parse
        con_5.execute(insert_5)

        for message in chat["messages"]:
            insert_51 = insert(TelegramMessage).values(
                telegram_id=message["id"],
                date=dateutil.parser.parse(message["date"]),
                unix_timestamp=message["date_unixtime"],
                from_name=message.get("from"),
                from_id=message.get("from_id"),
                chat_id=chat["id"],
            )  # (?) (error: NOT NULL constraint failed: telegram_message.id ) (hypothesis) Auto-increment is NOT working in "id" column
            con_5.execute(insert_51)
            if message["date"] < messages_min_date_confirmed:
                messages_min_date_confirmed = message["date"]
                print(messages_min_date_confirmed, "(inside the second 'for' cycle)") # (CDL) To confirm the 'if' condition above is never executed

        # (CDL)  UPDATE instead of INSERT
        # This block could be deleted in case we prove the "if" condition above is NOT necessary (aka can also be deleted)
        u = update(TelegramChat)
        updated_column_name = TelegramChat.messages_min_date_checked
        val = u.values({"updated_column_name":"messages_min_date_confirmed"})
        cond = val.where(TelegramChat.c.updated_column_name == "NULL")   #  Error: AttributeError: type object 'TelegramChat' has no attribute 'c'
        con_5.execute(cond)

        # insert_6 = insert(TelegramChat).values(
        #     messages_min_date_checked=messages_min_date_confirmed
        # )
        # result_6 = con_5.execute(insert_6)

        # print(messages_min_date_confirmed)

        con_5.commit()

        #            insert_51 = insert(TelegramMessage).values(id=message["id"], telegram_id=message["id"], date=dateutil.parser.parse(message["date"]), unix_timestamp=message["date_unixtime"], from_name=message.get("from"), from_id=message.get("from_id"), chat_id=chat["id"]) # This "crutch" experimental draft variant worked w/ NO errors
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
# con_5.commit()


# print(chat["type"])
# print(type(exported_data_dict["chats"]["list"]))
# ...??...

# (?) Try to delete 'text' module: is it vital here?

# (?!) Test what happens if I do NOT use colons in "VALUES" line

# Insert chat data (telegram_id, name, type) into SQLite:

# ins = students.insert().values(name = 'Ravi', lastname = 'Kapoor')   # (CDL) Example
# conn = engine.connect()
# result = conn.execute(ins)