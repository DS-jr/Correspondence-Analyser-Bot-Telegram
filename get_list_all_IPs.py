import json, psycopg2, hidden_2

conn_2 = psycopg2.connect(
	host=hidden_2.secrets_2()['host'], # Get secrets from hidden_2.py file about connection to the database 
	port=hidden_2.secrets_2()['port'],
	database=hidden_2.secrets_2()['database'],
	user=hidden_2.secrets_2()['user'])

cur_2 = conn_2.cursor()
# print(cur_2)
# print(type(cur_2))

var_1 = 'CREATE TABLE if not exists all_IP_addresses (id SERIAL, IP_address TEXT);'
cur_2.execute(var_1)
conn_2.commit()  # Flush to database server

with open('export_result_TG_account_N4.json', 'r') as json_file:
	nested_dict = json.load(json_file)
list_1 = nested_dict['other_data']['ips']
# print(list_1)

for dict_1 in list_1: 
	var_2 = 'INSERT INTO all_ip_addresses (ip_address) VALUES (%s);'
	cur_2.execute(var_2, (dict_1['ip'], ))
conn_2.commit() 

cur_2.execute('SELECT * FROM all_ip_addresses;') 
var_3 = cur_2.fetchall()
# print(type(var_3))
print('Updated database: ', var_3)  # To show the results via Terminal


	# print(dict_1['ip'])  # Get all IP addresses 
# var_2 = 'INSERT INTO all_ip_addresses (ip_address) VALUES ;'
# cur_2.execute(var_2)
# conn_2.commit()


# conn_1 = psycopg2.connect(
# 	host='localhost',
# 	port='5432',
# 	database='suppliers1',
# 	user='DS')
# cur_1 = conn_1.cursor()

# cur_1.execute('SELECT * FROM account;')
# a_1 = cur_1.fetchall() 
# print(a_1)
# print(type(a_1))


# print(cur_1)
# print(type(cur_1))


# list_2 = [ print(k['ip']) for k in nested_dict['other_data']['ips'] ]  # Alternative variant (it works fine & prints strings)

# hidden_2.json_file_export_TG_account_data

