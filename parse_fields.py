import json

with open("result.json") as f:
    data = json.load(f)


chat_fields = set()
message_fields = set()
text_entities_max_count = 0

for chat in data["chats"]["list"]:
    chat_fields |= set(chat.keys())
    for message in chat["messages"]:
        message_fields |= set(message.keys())
        if len(message['text_entities']) > text_entities_max_count:
            text_entities_max_count = len(message['text_entities'])
            print(message['id'])

print(chat_fields)
print(message_fields)
print(f'{text_entities_max_count=}')