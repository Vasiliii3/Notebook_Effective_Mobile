import os
import re
from typing import List, Tuple

from scripts.config import COUNTLIENS
from scripts.io import NAMECOLUMN


def clear_console():
    """Очищает консоль в зависимости от операционной системы."""
    os.system('cls' if os.name == 'nt' else 'clear')


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
    input('Нажмите Enter, чтобы выйти в меню')


def input_date():
    """Ввод всех данных для таблицы"""
    family = input("Введите фамилию ")
    name = input("Введите имя ")
    patronymic = input("Введите отчество ")
    name_organizations = input("Введите название организации ")
    phone_work = input("Введите телефон рабочий ")
    phone_mobile = input("Введите телефон личный(сотовый) ")
    return family, name, patronymic, name_organizations, phone_work, phone_mobile


def search_dictionary(data_table: list[dict]) -> list[tuple[int, dict]]:
    """По ключам ищет в списке словарей. На выходе кортеж"""
    print('Введите данные для поиска: ')
    data = input_date()
    search_criteria = {"Фамилия": data[0],
                       "Имя": data[1],
                       "Отчество": data[2],
                       "Название организации": data[3],
                       "Телефон рабочий": data[4],
                       "Телефон личный (сотовый)": data[5],
                       }
    result = []
    for count, item in enumerate(data_table):
        match = True
        # Проверка каждого критерия поиска на соответствие
        for key, search_value in search_criteria.items():
            if key in item and re.search(re.escape(search_value), item[key], re.IGNORECASE):
                continue
            else:
                match = False
                break
        if match:
            result.append((count, item))

    return result


def print_after_search(data):
    '''Вывод в консоль результата поиска'''
    print('№', *NAMECOLUMN, sep='\t')
    for count, val in enumerate(data, 1):
        print(count, *val[1].values(), sep='\t')