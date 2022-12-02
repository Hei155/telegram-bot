from telethon import TelegramClient, sync, events
from config import *
from operation import *


client = TelegramClient('session', API_ID, API_HASH)

numbers_data = open("./numbers/numbers.txt", 'r')
numbers = numbers_data.readlines()

for number in numbers:
    print(numbers)
    current_number = number.replace('8', '+7')

    @client.on(events.NewMessage(chats=current_number))
    async def normal_handler(event):
        await search_data(event.message.to_dict()['message'], event.message.to_dict()['peer_id']['user_id'], client)
        await add_number(event.message.to_dict()['message'], event.message.to_dict()['peer_id']['user_id'], client)
        await remove_number(event.message.to_dict()['message'], event.message.to_dict()['peer_id']['user_id'], client)

client.start()

client.run_until_disconnected()
