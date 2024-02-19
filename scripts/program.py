from scripts.constants import SETTING, GOODNEWTABLE, EMPTYBOOK, ALLVALUE, ADDVALUE
from scripts.io import newtable, read_table, add_value_table
from scripts.utils import clear_console, print_table


def settings() -> None:
    """Создание пустой книги если это нужно."""
    clear_console()
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
    clear_console()
    print(ALLVALUE)
    values = read_table()
    if not values:
        print(EMPTYBOOK)
        return
    return print_table(values)


def add_value_to_table() -> None:
    """Добавить значение из консоли в таблицу"""
    print(ADDVALUE)
    clear_console()
    family = input("Введите фамилию ")
    name = input("Введите имя ")
    patronymic = input("Введите отчество ")
    name_organizations = input("Введите название организации ")
    phone_work = input("Введите телефон рабочий ")
    phone_mobile = input("Введите телефон личный(сотовый) ")
    add_value_table(family, name, patronymic, name_organizations, phone_work, phone_mobile)
