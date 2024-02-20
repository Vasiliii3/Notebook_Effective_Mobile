from scripts.constants import SETTING, GOOD_NEW_TABLE, EMPTY_BOOK, ALL_VALUE, ADD_VALUE, GOOD_CHANGED, SEARCH_VALUE, \
    EDIT_VALUE
from scripts.io import new_table, read_table, add_value_table
from scripts.utils import clear_console, print_table, input_date, search_dictionary, print_after_search


def settings() -> None:
    """Создание пустой книги если это нужно."""
    clear_console()
    print(SETTING)
    print('Создать пустую адресную книг')
    while True:
        value = input('Введите да или нет, для выхода в меню\n').lower()
        if value == 'да':
            new_table()
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
    clear_console()
    print(SEARCH_VALUE)
    data = read_table()
    result = search_dictionary(data)
    if not result:
        print('Ничего не найдено')
        input('Нажмите Enter, чтобы выйти в меню')
        return
    print_after_search(result)
    input('Нажмите Enter, чтобы выйти в меню')


def edit_values_table() -> None:
    """Поиск и замена значение в таблице"""
    clear_console()
    print(EDIT_VALUE)
    data = read_table()
    result = search_dictionary(data)
    if not result:
        print('Ничего не найдено')
        input('Нажмите Enter, чтобы выйти в меню')
        return
    print_after_search(result)
    choice = int(input('Какую строку будем редактировать ? '))
    if choice > len(result) or choice < 0:
        print('Такой строки нету')
        return
    print('Введите новые данные если хотите поменять значения')
    string_selection = result[choice - 1][0]
    family = data[string_selection]['Фамилия']
    name = data[string_selection]['Имя']
    patronymic = data[string_selection]['Отчество']
    name_organizations = data[string_selection]['Название организации']
    phone_work = data[string_selection]['Телефон рабочий']
    phone_mobile = data[string_selection]['Телефон личный (сотовый)']
    data[string_selection]['Фамилия'] = input(family + ' ') or family
    data[string_selection]['Имя'] = input(name + ' ') or name
    data[string_selection]['Отчество'] = input(patronymic + ' ') or patronymic
    data[string_selection]['Название организации'] = input(name_organizations + ' ') or name_organizations
    data[string_selection]['Телефон рабочий'] = input(phone_work + ' ') or phone_work
    data[string_selection]['Телефон личный (сотовый)'] = input(phone_mobile + ' ') or phone_mobile
    new_table()
    for string in data:
        add_value_table(*string.values())
    print(GOOD_CHANGED)
    input('Нажмите Enter, чтобы выйти в меню')
