import requests
import bs4
from config import adminID
from utils.utils import *

def get_data(params):
    data = requests.get(f'https://www.google.com/search?q=site%3Ahttps%3A%2F%2Fwww.npi-tu.ru%2F+{params}')
    soup = bs4.BeautifulSoup(data.text, "html.parser")
    if soup.find('h3'):
        result = soup.find('h3').parent.parent.parent['href']
        return result[7:]
    else:
        return False


async def add_number(message, listener, client):
    letters_array = message.split(' ')
    if letters_array[0].lower() == '/добавить':
        if listener == adminID:
            if letters_array[1].lower()[0] == '+7':
                letters_array[1].lower()[0].replace('+7', '8')
            with open("./numbers/numbers.txt", "a") as nb:
                nb.write(letters_array[1].lower() + '\n')
            await client.send_message(listener, 'Вы добавили номер.')
        else:
            await client.send_message(listener, 'У Вас недостаточно прав.')


async def remove_number(message, listener, client):
    letters_array = message.split(' ')
    if letters_array[0].lower() == '/удалить':
        if listener == adminID:
            if letters_array[1].lower()[0] == '+7':
                letters_array[1].lower()[0].replace('+7', '8')
            f = open("./numbers/numbers.txt", "r")
            lines = f.readlines()
            f.close()
            if letters_array[1] + '\n' in lines:
                f = open("./numbers/numbers.txt", "w")
                for line in lines:
                    if line != letters_array[1].lower() + "\n":
                        f.write(line)
                f.close()
                await client.send_message(listener, 'Вы удалили номер.')
            else:
                await client.send_message(listener, 'Такого номера нет в списке добавленных!')
        else:
            await client.send_message(listener, 'У Вас недостаточно прав.')


async def search_data(message, listener, client):
    if message.split(' ')[0].lower() == '/найди':
        if len(message.split(' ')) < 2:
            await client.send_message(listener, 'Ваш запрос пустой.')
        else:
            key_array = message.split(' ')
            key_array.remove('/найди')
            key = ' '.join(key_array)
            if get_data(get_term(key)):
                href = get_data(key)
                await client.send_message(listener, f'По поводу «{key}» можно почитать: {href}')
            else:
                await client.send_message(listener, 'Информации по данному запросу нет.')