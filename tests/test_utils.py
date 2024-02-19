from src.utils import format_operation
from src.utils import sort_by_date


def test_sort_by_date():
    data = [
        {'date': '2021-01-01T12:00:00.000'},
        {'date': '2021-02-01T12:00:00.000'},
        {'date': '2021-03-01T12:00:00.000'}
    ]

    sorted_data = sort_by_date(data)

    assert len(sorted_data) == 3
    assert sorted_data[0]['date'] == '2021-03-01T12:00:00.000'
    assert sorted_data[1]['date'] == '2021-02-01T12:00:00.000'
    assert sorted_data[2]['date'] == '2021-01-01T12:00:00.000'


def test_format_operation():
    transaction = ({"id": 509552992, "state": "EXECUTED", "date": "2019-04-19T12:02:30.129240", "operationAmount":
                   {"amount": "81513.74", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод с карты на карту", "from": "Maestro 9171987821259925",
                    "to": "МИР 2052809263194182"})

    formatted_operation = format_operation(transaction)

    assert formatted_operation == ('19.04.2019 Перевод с карты на карту\n'
                                   'Maestro 91719 87** **** 9925 - МИР **4182\n'
                                   '81513.74 руб.')


def test_format_operation2():
    transaction = ({"id": 863064926, "state": "EXECUTED", "date": "2019-12-08T22:46:21.935582", "operationAmount":
                   {"amount": "41096.24", "currency": {"name": "USD", "code": "USD"}}, "description": "Открытие вклада",
                    "to": "Счет 90424923579946435907"})

    formatted_operation = format_operation(transaction)

    assert formatted_operation == ('08.12.2019 Открытие вклада\n'
                                   'Счет **5907\n'
                                   '41096.24 USD')


def test_format_operation3():
    transaction = ({"id": 482520625, "state": "EXECUTED", "date": "2019-11-13T17:38:04.800051", "operationAmount":
                   {"amount": "62814.53", "currency": {"name": "руб.", "code": "RUB"}}, "description":
                    "Перевод со счета на счет", "from": "Счет 38611439522855669794", "to": "Счет 46765464282437878125"})

    formatted_operation = format_operation(transaction)

    assert formatted_operation == ('13.11.2019 Перевод со счета на счет\n'
                                   'Счет 3861 1439 52** **** 9794 - Счет **8125\n'
                                   '62814.53 руб.')
