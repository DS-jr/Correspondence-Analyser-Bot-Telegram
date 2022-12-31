import json, psycopg2
import hidden_2  # hidden_2.py file in repo with secrets about connection to the database

conn_3 = psycopg2.connect(
    host=hidden_2.secrets_2()["host"],
    port=hidden_2.secrets_2()["port"],
    database=hidden_2.secrets_2()["database"],
    user=hidden_2.secrets_2()["user"],
)

cur_3 = conn_3.cursor()

with open("export_result_TG_account_N4.json", "r") as json_file:
    nested_dictionary_export = json.load(json_file)
# print(nested_dictionary_export)
# print(type(nested_dictionary_export))

list_3 = nested_dictionary_export["frequent_contacts"]["list"]
# print(list_3)
# print(type(list_3))

var_1 = """CREATE TABLE if not exists top_frequent_contacts (
    id SERIAL, 
    tg_id BIGINT UNIQUE, 
    tg_category VARCHAR(128), 
    tg_type VARCHAR(128), 
    tg_name VARCHAR(128), 
    tg_rating REAL, 
    PRIMARY KEY (id)
    );"""
cur_3.execute(var_1)
conn_3.commit()  # Flush to database server

for dict_3 in list_3:
    var_2 = "INSERT INTO top_frequent_contacts (tg_id, tg_category, tg_type, tg_name, tg_rating) VALUES (%s, %s, %s, %s, %s);"
    cur_3.execute(
        var_2,
        (
            dict_3["id"],
            dict_3["category"],
            dict_3["type"],
            dict_3["name"],
            dict_3["rating"],
        ),
    )
conn_3.commit()

cur_3.execute("SELECT * FROM top_frequent_contacts;")
var_4 = cur_3.fetchall()
# print(var_4)  # To show the results via Terminal


# for dict_3 in list_3:
# 	(dict_3['id'])
# 	(dict_3['category'])
# 	(dict_3['type'])
# 	(dict_3['name'])
# 	(dict_3['rating'])

# print(list_3[0]['id'])
# print(type(list_3[0]['id']))
# print(list_3[0]['rating'])
# print(type(list_3[0]['rating']))

# print(dict_3)
# print(type(dict_3))
