import csv
import os
from pathlib import Path

from scripts.config import FILE, DELIMITER, ENCODING
from scripts.constants import GOOD_RECODING

file = os.path.join(Path(__file__).parent.parent, FILE)

NAMECOLUMN = ["Фамилия", "Имя", "Отчество", "Название организации", "Телефон рабочий", "Телефон личный (сотовый)"]


def newtable():
    with open(file, mode="w", encoding=ENCODING) as w_file:
        names = NAMECOLUMN
        file_writer = csv.DictWriter(w_file, delimiter=DELIMITER, fieldnames=names, lineterminator="\r")
        file_writer.writeheader()
        print('')


def add_value_table(family: str, name: str, patronymic: str, name_organizations: str, phone_work: str, phone_mobile: str) -> None:
    """Записать значение в таблицу"""
    with open(FILE, mode="a", encoding=ENCODING) as w_file:
        names = NAMECOLUMN
        file_writer = csv.DictWriter(w_file, delimiter=DELIMITER, fieldnames=names, lineterminator="\r")
        file_writer.writerow({"Фамилия": family,
                              "Имя": name,
                              "Отчество": patronymic,
                              "Название организации": name_organizations,
                              "Телефон рабочий": phone_work,
                              "Телефон личный (сотовый)": phone_mobile,
                              })
    print(GOOD_RECODING)
    input('Нажмите Enter, чтобы выйти в меню')

def read_table() -> list[str]:
    """Чтение данных из файла в список"""
    with open(FILE, encoding='utf-8-sig') as r_file:
        file_reader = csv.DictReader(r_file, delimiter=DELIMITER)
        records = [row for row in file_reader]
    return records
