import json

with open("export_result_TG_account_N4.json", "r") as json_file:
    exported_data_nested_dict = json.load(json_file)

chat_id_input = input(
    "Paste Telegram chat-ID (numbers only) to export all previous data from this chat: "
)

for k in exported_data_nested_dict["chats"]["list"]:
    if chat_id_input == str(k["id"]):
        chat_data_json_string = json.dumps(k)
        print(
            "\nFound {} chat-ID among your chats. \nHere is all raw data from this chat: ".format(
                chat_id_input
            )
        )
        print(chat_data_json_string)

        # print(type(chat_data_json_string))
        # print(k)
        # print(type(k))

    # if chat_id_input != str(k["id"]):
    # 	break
    # else:
    # 	print('Found this chat-ID')

    # try:
    # 	chat_id_input == str(k["id"])
    # except:
    # 	print('NOT found this chat-ID')
    # else:
    # 	print('Found this chat-ID')


# all_chat_ids_list = []

# 	all_chat_ids_list.append(str(k["id"]))


# if chat_id_input in all_chat_ids_list:
# 	index_of_chat = ??
# 	print('Found this chat-ID')
# else:
#     print('NOT found this chat-ID')


# chat_id = k["id"]
# print(chat_id)
# print(all_chat_ids_list)

# number_of_chats = len(exported_data_nested_dict)

# print(exported_data_nested_dict["chats"]["list"])
# print(type(exported_data_nested_dict["chats"]["list"]))


# exported_data_string = json_file.read()
# print(exported_data_nested_dict)
# print(type(exported_data_nested_dict))


# print(chat_id_input)
# print(type(chat_id_input))
