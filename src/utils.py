import json
from datetime import datetime

# Открываем файл JSON
with open('Z:\projects\Diplom\Account transactions\data\operations.json', encoding='utf-8') as file:
    """"Выставить путь до данных через папку дата"""
    # Загружаем содержимое файла в переменную
    data = json.load(file)


def get_transaction():
    for transaction in data:
        return transaction


def format_operation(transaction):
    # Получаем дату из строки и преобразуем в нужный формат
    date = datetime.strptime(transaction['date'], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")

    # Получаем остальные данные операции
    description = transaction['description']
    from_ = ' '.join(transaction['from'].split(' ')[:-1])
    card = transaction['from'].split(' ')[-1]
    to_ = ' '.join(transaction['to'].split(' ')[:-1])
    account = transaction['to'].split(' ')[-1]
    amount = transaction['operationAmount']['amount'] + ' ' + transaction['operationAmount']['currency']['name']
    # Формируем отформатированную строку
    if from_ == 'Счет':
        formatted_operation = f'{date} {description}\n{from_} {card[0:4]} {card[4:8]} {card[8:10]}** **** {card[16:]} - {to_} **{account[-4:]}\n{amount}'
    else:
        formatted_operation = f'{date} {description}\n{from_} {card[0:5]} {card[5:7]}** **** {card[12:]} - {to_} **{account[-4:]}\n{amount}'

    return formatted_operation


print(format_operation(get_transaction()))
