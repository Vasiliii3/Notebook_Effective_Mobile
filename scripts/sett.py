import os

from scripts.constants import SETTING, GOODNEWTABLE
from scripts.io import newtable


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
