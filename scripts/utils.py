import os
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
