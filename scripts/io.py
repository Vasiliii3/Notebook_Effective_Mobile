import csv
import os
from pathlib import Path
from scripts.config import FILE, DELIMITER, ENCODING

file = os.path.join(Path(__file__).parent.parent, FILE)

NAME = ["Фамилия", "Имя", "Отчество", "Название организации", "Телефон рабочий", "Телефон личный (сотовый)"]


def newtable():
    with open(file, mode="w", encoding=ENCODING) as w_file:
        names = NAME
        file_writer = csv.DictWriter(w_file, delimiter=DELIMITER, fieldnames=names, lineterminator="\r")
        file_writer.writeheader()
        print('')


def addvalue():
    with open(FILE, mode="a", encoding=ENCODING) as w_file:
        names = NAME
        file_writer = csv.DictWriter(w_file, delimiter=DELIMITER, fieldnames=names, lineterminator="\r")
        file_writer.writerow({"Фамилия": "Петров2",
                              "Имя": "Ива",
                              "Отчество": "Кип",
                              "Название организации": "95",
                              "Телефон рабочий": "",
                              "Телефон личный (сотовый)": "2546",
                              })
