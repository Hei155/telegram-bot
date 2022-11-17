from telethon import TelegramClient, sync, events

api_id = 2458764
api_hash = '300ac6fbf3cc7f4872ed327e9b0d8c83'
allowedNumbers = ['+79525620964', '+79515313190']
admin = '+79515313190'
client = TelegramClient('session', api_id, api_hash)

import urllib3
import os.path
path = urllib3.util.parse_url('https://www.npi-tu.ru/university/about/').path
print(path)
while os.path.dirname(path) != '/':
    path = os.path.dirname(path)
    print(path)


async def add_number(message, listener):
    if message.lower() == '/добавить номер':
        await client.send_message('me', 'Введите номер по примеру: +7xxxxxxxxxx')
    if len(message) == 12 and message[0] == '+':
        try:
            num = int(message.replace('+7', '8'))
            await client.send_message(listener, 'Вы успешно добавили номер')
        except:
            await client.send_message(listener, 'Проверьте введенный номер')
    else:
        await client.send_message(listener, 'Проверьте введенный номер')

async def remove_number(message, listener):
    if message.lower() == '/удалить номер':
        await client.send_message('me', 'Введите номер по примеру: +7xxxxxxxxxx')
    if len(message) == 12 and message[0] == '+':
        try:
            num = int(message.replace('+7', '8'))
            await client.send_message(listener, 'Вы успешно удалили номер')
        except:
            await client.send_message(listener, 'Проверьте введенный номер')
    else:
        await client.send_message(listener, 'Проверьте введенный номер')

async def search_data(message, listener):
    letters_array = message.split(' ')
    key_array = message.split(' ')
    key_array.remove('/найди')
    key = ' '.join(key_array)
    if letters_array[0] == '/найди':
        await client.send_message(listener, f'По поводу <<{key}>> можно почитать в выпуске прошмандовки новочеркасска ')

for number in allowedNumbers:
    @client.on(events.NewMessage(chats=(number)))
    async def normal_handler(event):
        await search_data(event.message.to_dict()['message'], event.message.to_dict()['peer_id']['user_id'])

client.start()

client.run_until_disconnected()
