from scripts.constants import SETTING, GOOD_NEW_TABLE, EMPTY_BOOK, ALL_VALUE, ADD_VALUE
from scripts.io import newtable, read_table, add_value_table
from scripts.utils import clear_console, print_table, input_date, search_dictionary, print_after_search


def settings() -> None:
    """Создание пустой книги если это нужно."""
    clear_console()
    print(SETTING)
    print('Создать пустую адресную книг')
    while True:
        value = input('Введите да или нет, для выхода в меню\n').lower()
        if value == 'да':
            newtable()
            print(GOOD_NEW_TABLE)
        elif value == 'нет':
            return
        else:
            print('Неправильное значение')
            input('Нажмите Enter, чтобы продолжить...')


def print_table_for_file() -> list[str] | None:
    """Получение кортежа словаря из файла записной книжки"""
    clear_console()
    print(ALL_VALUE)
    values = read_table()
    if not values:
        print(EMPTY_BOOK)
        return
    return print_table(values)


def add_value_to_table() -> None:
    """Добавить значение из консоли в таблицу"""
    clear_console()
    print(ADD_VALUE)
    print('Введите данные для добавления: ')
    data = input_date()
    add_value_table(*data)


def search_in_table():
    """По ключам ищет в таблице. Результат выводит в консоль"""
    data = read_table()
    result = search_dictionary(data)
    print_after_search(result)