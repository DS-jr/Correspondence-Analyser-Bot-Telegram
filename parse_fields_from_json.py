# (task) Count the number of unique chats & messages in JSON
import json

with open("export_result_TG_account_N4.json") as json_file:
    data_dict = json.load(json_file)
    # print(type(data_dict))
    # print(data_dict)

number_of_chats = len(data_dict["chats"]["list"])
# print(type(number_of_chats))
# print(number_of_chats)

number_of_messages = 0
for chat in data_dict["chats"]["list"]:
    number_of_messages += len(chat["messages"]) # (?) Is this the most efficient way? ***(alternative) Taking the max 'id' value among all 'messages'?!

    #print(len(chat["messages"]))
#print(number_of_messages)



