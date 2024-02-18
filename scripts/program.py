import os

from scripts.constants import SETTING, GOODNEWTABLE, EMPTYBOOK, ALLVALUE, ADDVALUE
from scripts.io import newtable, read_table, NAMECOLUMN
from scripts.config import COUNTLIENS


def clear_console():
    """Очищает консоль в зависимости от операционной системы."""
    os.system('cls' if os.name == 'nt' else 'clear')


def settings() -> None:
    """Создание пустой книги если это нужно."""
    print(SETTING)
    print('Создать пустую адресную книг')
    while True:
        value = input('Введите да или нет\n').lower()
        if value == 'да':
            newtable()
            print(GOODNEWTABLE)
        elif value == 'нет':
            return
        else:
            print('Неправильное значение')
            input("Нажмите Enter, чтобы продолжить...")
            clear_console()


def print_table_for_file() -> list[str] | None:
    """Получение кортежа словаря из файла записной книжки"""
    print(ALLVALUE)
    values = read_table()
    if not values:
        print(EMPTYBOOK)
        return
    return print_table(values)


def print_table(values) -> None:
    """Вывод в консоли кортеж словарей и сортировка по Фамилии"""
    sort_values = sorted(values, key=lambda x: x['Фамилия'])
    print(*NAMECOLUMN, sep='\t')
    count = COUNTLIENS
    current = 0
    for val in sort_values:
        current += 1
        if current == count:
            b = input("Нажмите Enter, чтобы продолжить или напишите выход для выхода ").lower()
            if b == 'выход':
                break
            current = 0
        print(*val.values(), sep='\t')


def add_value_to_table():
    pass