import json
from datetime import datetime

# Открываем файл JSON
with open('Z:\projects\Diplom\Account transactions\data\operations.json', encoding='utf-8') as file:
    """"Выставить путь до данных через папку дата"""
    # Загружаем содержимое файла в переменную
    data = json.load(file)

def get_transactions():
    for transaction in data:
        return transaction


def format_operation(transaction):
    # Получаем дату из строки и преобразуем в нужный формат
    date = datetime.strptime(transaction['date'], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")

    # Получаем остальные данные операции
    description = transaction['description']
    card = transaction['from']
    account = transaction['to'].split(' ')[-1]
    amount = transaction['operationAmount']['amount'] + ' ' + transaction['operationAmount']['currency']['name']

    # Формируем отформатированную строку
    formatted_operation = f'{date} {description}\n{card} - Счет {account}\n{amount}'

    return formatted_operation

print(format_operation(get_transactions()))
