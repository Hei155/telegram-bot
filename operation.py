from config import allowedNumbers, adminID
import requests
import bs4


def get_data(params):
    data = requests.get(f'https://www.npi-tu.ru/search/index.php?q={params}&how=r', verify=False)
    soup = bs4.BeautifulSoup(data.text, "html.parser")
    for el in soup.find_all('td'):
        if el.find('a'):
            return el.find('a')['href']


async def add_number(message, listener, client):
    if listener == adminID:
        letters_array = message.split(' ')
        if letters_array[0].lower() == '/добавить':
            if letters_array[1].lower()[0] == '+7':
                letters_array[1].lower()[0].replace('+7', '8')
            allowedNumbers.append(letters_array[1].lower())
            await client.send_message(listener, 'Вы добавили номер.')
    else:
        await client.send_message(listener, 'У вас недостаточно прав.')


async def remove_number(message, listener, client):
    if listener == adminID:
        letters_array = message.split(' ')
        if letters_array[0].lower() == '/удалить':
            if letters_array[1].lower()[0] == '+7':
                letters_array[1].lower()[0].replace('+7', '8')
            if letters_array[1] in allowedNumbers:
                allowedNumbers.remove(letters_array[1].lower())
                await client.send_message(listener, 'Вы удалили номер.')
            else:
                await client.send_message(listener, 'Такой номер не был в списке добавленных!')
    else:
        await client.send_message(listener, 'У вас недостаточно прав.')


async def search_data(message, listener, client):
    if message.split(' ')[0].lower() == '/найди':
        key_array = message.split(' ')
        key_array.remove('/найди')
        key = ' '.join(key_array)
        if get_data(key):
            href = get_data(key)
            await client.send_message(listener, f'По поводу «{key}» можно почитать https://www.npi-tu.ru{href}')
        else:
            await client.send_message(listener, 'Информации по данному запросу нет.')