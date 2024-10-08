import json
from pathlib import Path


def load_json(file_path):
    """
     # Считывание json-файла

     :param file_path: путь к json-файлу
     :return: преобразованный из json-файла объект Python
     """
    with open(file_path, 'r') as file:
        return json.load(file)


def fill_values(tests, values_map):
    """
     # Заполнение пустых значений

     :param tests: данные из json-файла tests
     :param values_map: данные из json-файла values
     """
    for test in tests:
        test_id = test.get('id')
        # Заполнение значения для текущего теста
        if test_id in values_map:
            test['value'] = values_map[test_id]

        # Если есть вложенные тесты, заполняем их
        if 'values' in test:
            fill_values(test['values'], values_map)


def main(values_file, tests_file, report_file):
    """
     # Заполнение результрующего файла report

     :param values_file: путь к json-файлу values
     :param tests_file: путь к json-файлу tests
     :param tests_file: путь к json-файлу report
     """
    # Загружаем данные из файлов
    values_data = load_json(values_file)
    tests_data = load_json(tests_file)

    values_map = {item['id']: item['value'] for item in values_data['values']}

    fill_values(tests_data['tests'], values_map)

    # Записываем результат в report.json
    with open(report_file, 'w') as report_file_handle:
        json.dump(tests_data, report_file_handle, indent=4)


if __name__ == '__main__':
    values_path, tests_path, report_path = map(str, input('Введите путь/название файлов через пробел: ').split())

    main(values_path, tests_path, report_path)
    mypath = Path(report_path)
    if mypath.stat().st_size != 0:
        print('Запись в результирующий файл прошла успешно!')
    else:
        print('Ошибка записи!')
