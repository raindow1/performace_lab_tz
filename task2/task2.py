def read_circle(file_path):
    """
     # Считывание файла с координатами центра окружности и его радиусом

     :param file_path: путь к файлу
     :return: координаты центра и радиус
     """
    with open(file_path, 'r') as f:
        x, y = map(float, f.readline().strip().split())
        radius = float(f.readline().strip())
    return (x, y), radius


def read_points(file_path):
    """
     # Считывание файла с координатами точек

     :param file_path: путь к файлу
     :return: список с коррдинатами точек
     """
    with open(file_path, 'r') as f:
        points = [tuple(map(float, line.strip().split())) for line in f]
    return points


def position_relative_to_circle(circle_center, radius, points):
    """
     # Определение положения точки относительно окружности

     :param circle_center: координаты центра окружности
     :param radius: радиус окружности
     :param points: координаты точек
     :return: положения точек относительно окружности
     """
    results = []
    cx, cy = circle_center
    for px, py in points:
        distance_squared = (px - cx) ** 2 + (py - cy) ** 2
        if distance_squared < radius ** 2:
            results.append(1)  # точка внутри
        elif distance_squared > radius ** 2:
            results.append(2)  # точка снаружи
        else:
            results.append(0)  # точка на окружности
    return results


def main():

    print('!! Первым передаем файл с координатами центра окружности и его радиусом, вторым - с координатами точек !!')
    circle_file, points_file = map(str, input('Введите путь/название файлов через пробел: ').split())

    circle_center, radius = read_circle(circle_file)
    points = read_points(points_file)

    results = position_relative_to_circle(circle_center, radius, points)

    for result in results:
        print(result)


if __name__ == "__main__":
    main()