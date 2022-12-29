# (via Python)  In Postgres DB: create a new table (for putting data from “messages” section in JSON)
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

# var_1 = "INSERT INTO chats (name) VALUES ('v1 maNuaLLy aDDed nAme');"
# cursor_4.execute(var_1)
# connection_4.commit()


with open("export_result_TG_account_N4.json") as json_file:
    str_1 = json_file.read()
    export_data_to_dictionary = json.loads(str_1)
    # print(type(export_data_to_dictionary))
    # print(type(str_1))

list_of_chats = export_data_to_dictionary["chats"]["list"]
# print(list_of_chats)
# print(type(list_of_chats))
for chat in list_of_chats:
    message_data = chat["messages"]
    for parameters in message_data:
        message_date = parameters["date"]
        message_text = parameters["text"]  # ?! The output may be a string OR a list with strings / dicts
        # print(message_text)
        # print(type(message_text))

        # print(message_date)
        # print(type(message_date))

        # print(parameters)
        # print(type(parameters))

    # print(message_data)
    # print(type(message_data))
    #print(type(chat))

