import json
# Открываем файл JSON
with open('Z:\projects\Diplom\Account transactions\data\operations.json', encoding='utf-8') as file:
    """"Выставить путь до данных через папку дата"""
    # Загружаем содержимое файла в переменную
    data = json.load(file)

def get_last_transactions():
    for transaction in data:
        print(transaction)
        return transaction


get_last_transactions()