import json, psycopg2, os
from dotenv import load_dotenv

load_dotenv()

connection_4 = psycopg2.connect(
    host=os.getenv("HOST"),
    port=os.getenv("PORT"),
    database=os.getenv("DATABASE"),
    user=os.getenv("USER")
)

cursor_4 = connection_4.cursor()

with open("export_result_TG_account_N4.json") as json_file:
    str_1 = json_file.read()
    export_data_to_dictionary = json.loads(str_1)

list_of_chats = export_data_to_dictionary["chats"]["list"]

# for chat in list_of_chats:
#     message_data = chat["messages"]
#     for parameters in message_data:
#         message_date = parameters["date"]
#         message_text = parameters["text"]  # (?) The output may be a string OR a list with strings / dicts

# + (via Python)  In Postgres DB: create a new table with necessary columns for putting data from JSON’s “messages” section
create_table_messages = """CREATE TABLE if not exists messages_1 (
                        id SERIAL,
                        tgmessageid INTEGER UNIQUE,
                        type VARCHAR(32),
                        date VARCHAR(128),
                        date_unixtime VARCHAR(128),
                        fromname VARCHAR(128),
                        fromid VARCHAR(128),
                        text VARCHAR,
                        PRIMARY KEY (id)
                        );"""
# (?)  Did I choose data types correctly? Can some parts be done in a better / leaner way?
# (?) 'text' column: The output may be a string OR a list with strings / dicts.  ***(also) Is 'TEXT' data type better than VARCHAR here?
# (?)  "text_entities" sub-section in “messages”: shall I use the data from it & put it to DB?  ***It’s gonna be a mess.   ***As for now I’ve skipped it.
cursor_4.execute(create_table_messages)
connection_4.commit()


# ! (via Python)  Send “tgmessageid” data from “messages” section in the Dictionary to the target table already created in the DB
for chat in export_data_to_dictionary["chats"]["list"]:
    for message_parameter in chat["messages"]:
        var_3 = "INSERT INTO messages_1 (tgmessageid, type, date, date_unixtime, fromname, fromid) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor_4.execute(var_3, (message_parameter["id"], message_parameter["type"], message_parameter["date"], message_parameter["date_unixtime"], message_parameter["from"], message_parameter["from_id"]))
        # var_1 = message_parameter["id"]
        # var_2 = "INSERT INTO messages_1 (tgmessageid) VALUES (var_1);" # (?) Why does this line create an error?  ***psycopg2.errors.UndefinedColumn: column "var_1" does not exist
        # cursor_4.execute(var_2)
connection_4.commit()


        # print(message_text)
        # print(type(message_text))

        # print(message_date)
        # print(type(message_date))

        # print(parameters)
        # print(type(parameters))

    # print(message_data)
    # print(type(message_data))
    #print(type(chat))

# print(list_of_chats)
# print(type(list_of_chats))


# var_1 = "INSERT INTO chats (name) VALUES ('v1 maNuaLLy aDDed nAme');"
# cursor_4.execute(var_1)
# connection_4.commit()

# print(type(export_data_to_dictionary))
# print(type(str_1))
