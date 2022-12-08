import hidden_2, psycopg2

connection_1 = psycopg2.connect(
    host=hidden_2.secrets_2()["host"],
    port=hidden_2.secrets_2()["port"],
    database=hidden_2.secrets_2()["database"],
    user=hidden_2.secrets_2()["user"]
)

cur_1 = connection_1.cursor()


var_3 = "CREATE TABLE if not exists Contacts_users (id SERIAL, tg_ids BIGINT UNIQUE);"
cur_1.execute(var_3)
connection_1.commit()

# (w/ Python) Insert pieces of data to this table

var_4 = "INSERT INTO Contacts_users (tg_ids) VALUES (56789);"
cur_1.execute(var_4)
connection_1.commit()


# (w/ Python) Select all data from an existing table & print it
# cur_1.execute("SELECT * FROM all_ip_addresses;")
# var_2 = cur_1.fetchall()
#print(var_2)
#print(var_1)


# (w/ Python) Connect to a DB in Postgres
# (w/ Python) Create a new table in Postgres w/ necessary columns




