# ! (extract from JSON) List of ALL ‘ip addresses’ used by your TG account during the last 12 months.  
# ***In JSON export check sections: ‘other data’ - ‘ips’

import json

# hidden_2.json_file_export_TG_account_data
with open('export_result_TG_account_N4.json', 'r') as json_file:
	nested_dict = json.load(json_file)
	# string_1 = json_file.read()
# print(nested_dict)
# print(type(nested_dict))

list_1 = nested_dict['other_data']['ips']
for ip_address in list_1: 
	print(ip_address['ip'])  # Get all IP addresses 

# list_2 = [ print(k['ip']) for k in nested_dict['other_data']['ips'] ]  # Is this a 'good practice' solution? (it works fine & prints strings)

#	print(type(k['ip']))
# ip_addresses
# print(ip_addresses)
# print(type(ip_addresses))
