import json
import os
from datetime import datetime


def print_first_5_transactions():
    # Открываем файл JSON
    with open(os.path.join("..", "data", "operations.json"), encoding='utf-8') as file:
        # Загружаем содержимое файла в переменную
        data = json.load(file)

    # Выводим первые 5 транзакций
    for transaction in data:
        print(f'{format_operation(transaction)}\n')


def format_operation(transaction):
    if transaction != {}:
        # Получаем дату из строки и преобразуем в нужный формат
        date = datetime.strptime(transaction['date'], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        # Получаем остальные данные операции
        description = transaction['description']
        to_ = ' '.join(transaction['to'].split(' ')[:-1])
        account = transaction['to'].split(' ')[-1]
        amount = transaction['operationAmount']['amount'] + ' ' + transaction['operationAmount']['currency']['name']
        if description != "Открытие вклада":
            from_ = ' '.join(transaction['from'].split(' ')[:-1])
            card = transaction['from'].split(' ')[-1]
            # Формируем отформатированную строку
            if from_ == 'Счет':
                formatted_operation = f'{date} {description}\n{from_} {card[0:4]} {card[4:8]} {card[8:10]}** **** {card[16:]} - {to_} **{account[-4:]}\n{amount}'
            else:
                formatted_operation = f'{date} {description}\n{from_} {card[0:5]} {card[5:7]}** **** {card[12:]} - {to_} **{account[-4:]}\n{amount}'
            return formatted_operation
        else:
            to_ = ' '.join(transaction['to'].split(' ')[:-1])
            # Формируем отформатированную строку
            formatted_operation = f'{date} {description}\n{to_} **{account[-4:]}\n{amount}'
            return formatted_operation


print_first_5_transactions()
