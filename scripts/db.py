import os

from scripts.constants import SETTING, GOODNEWTABLE, EMPTYBOOK
from scripts.io import newtable, read_table


def clear_console():
    """Очищает консоль в зависимости от операционной системы."""
    os.system('cls' if os.name == 'nt' else 'clear')


def settings():
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


def print_table(values):
    if not values:
        print(EMPTYBOOK)
        return
    for row in values:
        print(row)

