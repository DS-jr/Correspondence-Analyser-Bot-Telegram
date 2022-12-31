import os, json, psycopg2
from dotenv import load_dotenv

load_dotenv()

with open("export_result_TG_account_N4.json") as json_export_file:
    correspondence_export_dictionary = json.load(json_export_file)
    # print(type(dict_3))
    # a_1 = json_export.read()
    # print(type(a_1))

connection_3 = psycopg2.connect(
    host=os.getenv("HOST"),
    port=os.getenv("PORT"),
    database=os.getenv("DATABASE"),
    user=os.getenv("USER"),
)

cur_3 = connection_3.cursor()

#  (w/ Python) Create a new table in Postgres w/ three columns about "chats"
var_2 = "CREATE TABLE if not exists chats (id SERIAL, name VARCHAR(128), type VARCHAR(32), tgchatid INTEGER, UNIQUE(tgchatid), PRIMARY KEY(id) );"
cur_3.execute(var_2)
connection_3.commit()


# (TASK) (w/ Python) Insert all the selected CHAT IDs to this table
for chat in correspondence_export_dictionary["chats"]["list"]:
    var_5 = "INSERT INTO chats (name, type, tgchatid) VALUES (%s, %s, %s);"
    cur_3.execute(var_5, (chat.get("name", "NA"), chat.get("type"), chat.get("id")))

    # var_4 = "INSERT INTO chats (name) VALUES (%s);"
    # cur_3.execute(var_4, (chat.get('name', 'NA'),))

    # var_4 = "INSERT INTO chats (tgchatid) VALUES (%s);"
    # cur_3.execute(var_4, (chat.get('id'),))

    # var_4 = "INSERT INTO chats (type) VALUES (%s);"
    # cur_3.execute(var_4, (chat.get('type', 'NA'),)) # This line worked!  Pay attention to the comma between parenthesis at the end

    # var_4 = "INSERT INTO chats (name, type, tgchatid) VALUES (%s, %s, %s);"
    # cur_3.execute(var_4, (chat.get('name'), chat.get('type'), chat.get('id')))

    # print(chat.get('messages'))
    # print(chat.get('id', 'NA'), chat.get('type', 'NA'), chat.get('name', 'NA'))
    # print(chat.get('name'))
    # print(f"name: {chat.get('name', 'NA')}")
    # print(chat['name'])
    # print(type(chat))
connection_3.commit()


# Variant 1:
# for k in dict_3["chats"]["list"]:  # (CDL) Adding "if True" condition below is important, as it's better to check if every key exists in every dict
#     if k['']:  # (?) How to bypass the error here?  ***"Saved messages" chat's dictionary has NO key "name"
#         print('yes')
#     else:
#         pass
# print(type(k))
# var_3 = "INSERT INTO v1_tg_data_export(name, type, tgchatid) VALUES(%s, %s, %s)"
# cur_3.execute()
# if k['type'] in dict_3["chats"]["list"]:

# Variant 2:
# (!) Proceed from here:
# for k in range():  #  Try a temporary solution: exclude "Saved messages" chat


# a_1 = dict_3["chats"]["list"][1]["id"]
# print(a_1)

# var_1 = "INSERT INTO contacts_users (tg_ids) VALUES (78901);"
# cur_3.execute(var_1)
# connection_3.commit()

# (via Python) Add manually a new row to an existing table in the DB

# print(dict_3["contacts"]["list"][0]["phone_number"])

# var_4 = "INSERT INTO contacts_users (tg_ids) VALUES (89012);"
# cur_3.execute(var_4)
# connection_3.commit()
