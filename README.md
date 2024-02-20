# Тестовое задание компании Effective Mobile

## Описание задания

### Реализовать телефонный справочник со следующими возможностями:

1. Вывод постранично записей из справочника на экран
2. Добавление новой записи в справочник
3. Возможность редактирования записей в справочнике
4. Поиск записей по одной или нескольким характеристикам

### Требования к программе:

1. Реализация интерфейса через консоль (без веб- или графического интерфейса)
2. Хранение данных должно быть организовано в виде текстового файла, формат которого придумывает сам программист
3. В справочнике хранится следующая информация: фамилия, имя, отчество, название организации, телефон рабочий, телефон личный (сотовый)

### Плюсом будет:

1. Аннотирование функций и переменных
2. Документирование функций
3. Подробно описанный функционал программы
4. Размещение готовой программы и примера файла с данными на github

## Требования

* Python 3.10 и выше

## Установка

* `git clone https://github.com/Vasiliii3/Notebook_Effective_Mobile.git`
* Для запуска скрипта
*  `python main.py`

* При необходимости создайте вирутальное окружение, например можно использовать для этого переходим в папку с 
  проектом и создаем окружение
* `python -m venv venv`
* Для активации используем
* * Для Для Windows: `venv\Scripts\activate`
* * Для macOS и Linux: `source venv/bin/activate'
* Потом запускаем сам скрипт 

## Особенности

* В корневой директории проекта находятся файл с данными и файл с настройками -- `notebook.txt` и `settings.ini` 
  соответственно, и файл пример для первичного теста скрипта `notebook demo.txt`
* В случае отсутствия файла с данными можно создать через скрипт меню настройки
* При поиске не учитываются регистр слов, так же можно искать по неполному вхождению слов.

## Настройки

Настройка программы осуществляется путём изменения расположенного в корневой директории файла `settings.ini`

* `Name` - имя которое будет выводится при запуске
* * По умолчанию пусто
* `CountLines` - сколько строк выводит при выводе справочника
* * По умолчанию значение 5
