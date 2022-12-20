import requests
import bs4
from config import adminID
from utils.utils import get_term
from rutermextract import TermExtractor
term_extractor = TermExtractor()

# Парсинг запроса


def get_data(params):
    data = requests.get(f'https://www.google.com/search?q=site%3Ahttps%3A%2F%2Fwww.npi-tu.ru%2F+{params}')
    soup = bs4.BeautifulSoup(data.text, "html.parser")
    if soup.find('h3'):
        result = soup.find('h3').parent.parent.parent['href'][7:]
        url = result[7:]
        return url[:url.find('&')]
    else:
        return False

# Добавление номера


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


# Удаление номера


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


# Поиск информации по запросу

async def search_data(message, listener, client):
    key_words = get_term(message)
    response = get_data(key_words)
    if response:
        await client.send_message(listener, f'По поводу «{message}» можно почитать: {response}')
    else:
        await client.send_message(listener, 'Информации по данному запросу нет.')