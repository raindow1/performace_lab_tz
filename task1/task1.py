def circular_list(n, m):
    """
     Создание кругового массива

     :param n: длина массива
     :param m: длина интервала
     :return: искомый путь
     """
    circular_list = list(range(1, n + 1))

    # Переменная для хранения начальных элементов интервалов
    result_path = []

    start_index = 0

    while True:
        # Определяем конечный индекс текущего интервала
        end_index = (start_index + m - 1) % n

        # Добавляем начальный элемент интервала в путь
        result_path.append(circular_list[start_index])

        if end_index == 0:
            break

        start_index = end_index

    return result_path


if __name__ == '__main__':
    n, m = map(int, input('Введите n и m через пробел:').split())
    result = circular_list(n, m)
    print('Путь:')
    for a in result:
        print(a, end='')

