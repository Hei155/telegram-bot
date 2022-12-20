from telethon import TelegramClient, sync, events
from config import *
from operation import search_data


client = TelegramClient('session', API_ID, API_HASH)


@client.on(events.NewMessage(chats=numbers))
async def normal_handler(event):
    await search_data(event.message.to_dict()['message'], event.message.to_dict()['peer_id']['user_id'], client)
    # await add_number(event.message.to_dict()['message'], event.message.to_dict()['peer_id']['user_id'], client)
    # await remove_number(event.message.to_dict()['message'], event.message.to_dict()['peer_id']['user_id'], client)

client.start()

client.run_until_disconnected()
