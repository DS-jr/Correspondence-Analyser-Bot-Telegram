import json 

with open('export_result_TG_account_N4.json', 'r') as json_file:
    dict_3 = json.load(json_file)  #  Load JSON file directly to a Python dictionary 
# print(type(dict_3))

about_section_value = dict_3['about']
# print(about_section_value)
# print(type(about_section_value))

first_name_value = dict_3['contacts']['list'][1]['first_name']
# print(first_name_value)
# print(type(first_name_value))

last_active_values = dict_3["sessions"]["list"][0]["last_active"]
# print(last_active_values)
# print(type(last_active_values))

for k in dict_3["sessions"]["list"]:
    print(k["last_active"])
    # print(type(k["last_active"]))

# c_1 = open('export_result_TG_account_N4.json')
# string_1 = c_1.read()
# print(type(string_1))

# dict_1 = json.loads(string_1)
# print(dict_1)
# print(type(dict_1))

# dict_2 = json.load(c_1)
# print(dict_2)
# print(type(dict_2))
