from scripts.constants import GREETING, CHOICES
from scripts.program import settings, clear_console, print_table_for_file, add_value_to_table


def main():
    print(GREETING)
    while True:
        print(CHOICES)
        value = int(input())
        match value:
            case 1:
                settings()
            case 2:
                print_table_for_file()
            case 3:
                add_value_to_table()
            case 4:
                pass
            case 5:
                pass
            case 6:
                return
            case _:
                print('Неправильное значение')
                input("Нажмите Enter, чтобы продолжить...")
                clear_console()


if __name__ == '__main__':
    main()