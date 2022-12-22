import json, psycopg2
import hidden_3

with open("export_result_TG_account_N4.json") as json_export_file:
    dict_3 = json.load(json_export_file)
    # print(type(dict_3))
    # a_1 = json_export.read()
    # print(type(a_1))

for k in dict_3["chats"]["list"]:
    print(k["id"])

connection_3 = psycopg2.connect(
    host=hidden_3.secrets_3()["host"],
    port=hidden_3.secrets_3()["port"],
    database=hidden_3.secrets_3()["database"],
    user=hidden_3.secrets_3()["user"]
)

cur_3 = connection_3.cursor()


# var_1 = "INSERT INTO contacts_users (tg_ids) VALUES (78901);"
# cur_3.execute(var_1)
# connection_3.commit()

# (via Python) Add manually a new row to an existing table in the DB

#a_1 = dict_3["chats"]["list"][1]["id"]
#print(a_1)
