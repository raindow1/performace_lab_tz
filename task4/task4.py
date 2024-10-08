def read_file(filename):
    """
     # Считывание файла с числами

     :param filename: путь к файлу
     :return: список чисел
     """
    with open(filename, 'r') as file:
        return [int(line.strip()) for line in file.readlines()]


def minimum_moves(numbers):
    """
     # Нахождение минимального кол-ва шагов

     :param numbers: список чисел
     :return: минимальное необходимое кол-во шагов
     """
    numbers.sort()
    # Нахождение медианы
    median = numbers[len(numbers) // 2]
    return sum(abs(num - median) for num in numbers)


if __name__ == "__main__":
    input_file = input('Введите путь/название файла: ')
    numbers = read_file(input_file)
    result = minimum_moves(numbers)
    print(result)