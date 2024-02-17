import json
import os
from utils import sort_by_date
from utils import format_operation

def print_sorted_transactions():
    # Открываем файл JSON
    with open(os.path.join("..", "data", "operations.json"), encoding='utf-8') as file:
        # Загружаем содержимое файла в переменную
        data = json.load(file)
        # Сортируем данные по дате
        sorted_data = sort_by_date(data)
        # Выводим отсортированные транзакции
        for transaction in sorted_data[:5]:
            print(f'{format_operation(transaction)}\n')

print_sorted_transactions()