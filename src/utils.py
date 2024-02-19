from datetime import datetime


def sort_by_date(data):
    """Сортируем данные по дате"""
    sorted_data = sorted([x for x in data if x.get('date')],
                         key=lambda x: datetime.strptime(x.get('date', ''), "%Y-%m-%dT%H:%M:%S.%f"),
                         reverse=True)
    return sorted_data


def format_operation(transaction):
    """Приводит отдельную транзакцию в нужный формат и выводит"""
    date = datetime.strptime(transaction['date'], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
    description = transaction['description']
    to_ = ' '.join(transaction['to'].split(' ')[:-1])
    account = transaction['to'].split(' ')[-1]
    amount = transaction['operationAmount']['amount'] + ' ' + transaction['operationAmount']['currency']['name']
    if description != "Открытие вклада":
        from_ = ' '.join(transaction['from'].split(' ')[:-1])
        card = transaction['from'].split(' ')[-1]
        if from_ == 'Счет':
            formatted_operation = (f'{date} {description}\n{from_} '
                                   f'{card[0:4]} {card[4:8]} {card[8:10]}** **** {card[16:]} - '
                                   f'{to_} **{account[-4:]}\n{amount}')
        else:
            formatted_operation = (f'{date} {description}\n{from_} '
                                   f'{card[0:5]} {card[5:7]}** **** {card[12:]} - '
                                   f'{to_} **{account[-4:]}\n{amount}')
        return formatted_operation
    else:
        to_ = ' '.join(transaction['to'].split(' ')[:-1])
        formatted_operation = f'{date} {description}\n{to_} **{account[-4:]}\n{amount}'
        return formatted_operation
