#файл points.py
def scale_points(points, factor):
    """
    Умножает все координаты на factor.
    Использует map и lambda.
    
    Параметры:
    - points: список точек [(x1, y1), (x2, y2), ...]
    - factor: коэффициент масштабирования
    
    Возвращает:
    - Новый список точек с масштабированными координатами
    
    Пример использования map и lambda:
    map(lambda p: (p[0] * factor, p[1] * factor), points)
    """
    if not points:
        raise EmptyPointsListException()
    
    return list(map(lambda p: (p[0] * factor, p[1] * factor), points))


def filter_points_by_quadrant(points, quadrant):
    """
    Фильтрует точки по квадранту (1-4).
    Использует filter и lambda.
    
    Параметры:
    - points: список точек
    - quadrant: номер квадранта (1-4)
    
    Возвращает:
    - Отфильтрованный список точек в указанном квадранте
    
    Квадранты:
    1: x >= 0, y >= 0
    2: x < 0, y >= 0
    3: x < 0, y < 0
    4: x >= 0, y < 0
    
    Пример использования filter и lambda для разных условий
    """
    if not points:
        raise EmptyPointsListException()
    
    if quadrant == 1:
        return list(filter(lambda p: p[0] >= 0 and p[1] >= 0, points))
    elif quadrant == 2:
        return list(filter(lambda p: p[0] < 0 and p[1] >= 0, points))
    elif quadrant == 3:
        return list(filter(lambda p: p[0] < 0 and p[1] < 0, points))
    elif quadrant == 4:
        return list(filter(lambda p: p[0] >= 0 and p[1] < 0, points))
    else:
        raise ValueError("Квадрант должен быть от 1 до 4")
    

    def calculate_total_vector(points):
    """
    Суммирует все точки как векторы.
    Использует reduce и lambda.
    
    Параметры:
    - points: список точек
    
    Возвращает:
    - Кортеж (sum_x, sum_y) - сумма всех координат
    
    Пример использования reduce:
    reduce(lambda acc, p: (acc[0] + p[0], acc[1] + p[1]), points)
    
    Начинает с (0, 0) и последовательно складывает координаты
    """
    if not points:
        return (0, 0)
    
    return reduce(
        lambda acc, p: (acc[0] + p[0], acc[1] + p[1]),
        points
    )


def sort_points_by_custom_criteria(points, criteria="distance_to_origin"):
    """
    Сортирует точки по разным критериям.
    Использует sorted с lambda ключами.
    
    Параметры:
    - points: список точек
    - criteria: критерий сортировки
    
    Возвращает:
    - Отсортированный список точек
    
    Критерии:
    - distance_to_origin: по расстоянию до начала координат
    - x_then_y: сначала по X, потом по Y
    - y_then_x: сначала по Y, потом по X
    - sum_coordinates: по сумме координат
    
    Примеры lambda как ключа сортировки
    """
    if not points:
        raise EmptyPointsListException()
    
    if criteria == "distance_to_origin":
        return sorted(points, key=lambda p: math.sqrt(p[0]**2 + p[1]**2))
    elif criteria == "x_then_y":
        return sorted(points, key=lambda p: (p[0], p[1]))
    elif criteria == "y_then_x":
        return sorted(points, key=lambda p: (p[1], p[0]))
    elif criteria == "sum_coordinates":
        return sorted(points, key=lambda p: p[0] + p[1])
    else:
        raise ValueError(f"Неизвестный критерий сортировки: {criteria}")
    

    def transform_points_with_pipeline(points, transformations):
    """
    Применяет цепочку преобразований к точкам.
    Пример функционального пайплайна.
    
    Параметры:
    - points: список точек
    - transformations: список функций-преобразований
    
    Возвращает:
    - Точки после применения всех преобразований
    
    Пример пайплайна:
    transformations = [
        lambda p: (p[0] + 1, p[1] + 1),
        lambda p: (p[0] * 2, p[1] * 2)
    ]
    Результат: каждая точка сначала сдвигается, потом масштабируется
    """
    if not points:
        raise EmptyPointsListException()
    
    result = points
    for transform_func in transformations:
        result = list(map(transform_func, result))
    
    return result


def find_all_distances_between_points(points):
    """
    Находит все расстояния между парами точек.
    Использует комбинации и map.
    
    Параметры:
    - points: список точек
    
    Возвращает:
    - Список кортежей (точка1, точка2, расстояние)
    
    Пример использования map с combinations:
    map(lambda pair: (pair[0], pair[1], distance), combinations(points, 2))
    """
    from itertools import combinations
    
    if len(points) < 2:
        raise InsufficientPointsException(required=2, actual=len(points))
    
    point_pairs = combinations(points, 2)
    
    distances = list(map(
        lambda pair: (pair[0], pair[1], math.sqrt(
            (pair[1][0] - pair[0][0])**2 + (pair[1][1] - pair[0][1])**2
        )),
        point_pairs
    ))
    
    return distances


#файл distance.py
def find_all_closest_points(points):
    """
    Для каждой точки находит ближайшую.
    Использует map для преобразования.
    
    Параметры:
    - points: список точек
    
    Возвращает:
    - Список кортежей (исходная_точка, ближайшая_точка)
    
    Пример использования map с существующей функцией find_closest:
    map(lambda target: (target, find_closest(target, points)), points)
    """
    if len(points) < 2:
        raise InsufficientPointsException(required=2, actual=len(points))
    
    closest_points = list(map(
        lambda target: (target, find_closest(target, points)),
        points
    ))
    
    return closest_points


def calculate_total_distance(points):
    """
    Вычисляет общее расстояние при обходе точек по порядку.
    Использует reduce для аккумуляции расстояний.
    
    Параметры:
    - points: список точек в порядке обхода
    
    Возвращает:
    - Суммарное расстояние пути через все точки
    
    Пример сложной аккумуляции с reduce:
    reduce(функция_аккумулятор, points[1:], (0, первая_точка))
    """
    if len(points) < 2:
        return 0
    
    def distance_accumulator(acc, current_point):
        """Вспомогательная функция для reduce."""
        total_distance, prev_point = acc
        distance = calc_dist(prev_point, current_point)
        return (total_distance + distance, current_point)
    
    initial_state = (0, points[0])
    
    total_distance, _ = reduce(
        distance_accumulator,
        points[1:],
        initial_state
    )
    
    return total_distance


def filter_points_by_distance(points, reference_point, max_distance):
    """
    Фильтрует точки по расстоянию до reference_point.
    Использует filter и lambda.
    
    Параметры:
    - points: список точек
    - reference_point: точка отсчета
    - max_distance: максимальное расстояние
    
    Возвращает:
    - Точки, находящиеся не дальше max_distance от reference_point
    
    Пример использования filter с вычислением в lambda:
    filter(lambda p: calc_dist(p, reference_point) <= max_distance, points)
    """
    if not points:
        raise InsufficientPointsException(required=1, actual=0)
    
    return list(filter(
        lambda p: calc_dist(p, reference_point) <= max_distance,
        points
    ))


#файл menu_state.py
async def _functional_operations(self):
    """
    Демонстрация всех функциональных операций с точками.
    Показывает примеры использования map, filter, reduce, lambda.
    
    Выполняет последовательно:
    1. Масштабирование (map)
    2. Фильтрацию (filter)
    3. Суммирование векторов (reduce)
    4. Сортировку (sorted + lambda)
    5. Вычисление всех расстояний (combinations + map)
    """
    if not self.context.points:
        print("\nНет точек для операций!")
        print("Сначала введите точки (выберите пункт 1)")
        return
    
    print("\n" + "="*40)
    print("ФУНКЦИОНАЛЬНЫЕ ОПЕРАЦИИ С ТОЧКАМИ")
    print("="*40)
    print("Исходные точки:", self.context.points)
    print("-"*40)
    
    try:
        # 1. Масштабирование точек (map)
        scaled = scale_points(self.context.points, 2)
        print("1. Масштабирование в 2 раза (map):", scaled)
        
        # 2. Фильтрация по квадранту (filter)
        quadrant1_points = filter_points_by_quadrant(self.context.points, 1)
        print("2. Точки в 1-м квадранте (filter):", quadrant1_points)
        
        # 3. Суммарный вектор (reduce)
        total_vector = calculate_total_vector(self.context.points)
        print("3. Суммарный вектор всех точек (reduce):", total_vector)
        
        # 4. Сортировка по расстоянию до начала координат (sorted с lambda)
        sorted_points = sort_points_by_custom_criteria(self.context.points, "distance_to_origin")
        print("4. Сортировка по расстоянию до (0,0) (sorted + lambda):", sorted_points)
        
        # 5. Все расстояния между точками (combinations + map)
        if len(self.context.points) >= 2:
            distances = find_all_distances_between_points(self.context.points)
            print("5. Все расстояния между точками (combinations + map):")
            for p1, p2, dist in distances:
                print(f"   {p1} -> {p2}: {dist:.2f}")
        
    except Exception as e:
        print(f"Ошибка при выполнении операций: {e}")
    
    print("\nНажмите Enter для продолжения...")
    input()


    #файл process_state.py
    # В методе handle_input добавлены обработчики для новых опций:

elif choice == '5':  # Масштабирование (map)
    self.context.method = "scale"
    factor = float(input("Введите коэффициент масштабирования: "))
    self.context.result = scale_points(self.context.points, factor)
    print(f"Масштабирование в {factor} раз выполнено")

elif choice == '6':  # Фильтрация (filter)
    self.context.method = "filter_quadrant"
    quadrant = int(input("Введите квадрант (1-4): "))
    self.context.result = filter_points_by_quadrant(self.context.points, quadrant)
    print(f"Фильтрация по квадранту {quadrant} выполнена")

elif choice == '7':  # Суммирование (reduce)
    self.context.method = "total_vector"
    self.context.result = calculate_total_vector(self.context.points)
    print("Вычисление суммарного вектора выполнено")

elif choice == '8':  # Сортировка (sorted + lambda)
    self.context.method = "sort"
    criteria = input("Критерий сортировки (distance_to_origin/x_then_y/y_then_x/sum_coordinates): ")
    self.context.result = sort_points_by_custom_criteria(self.context.points, criteria)
    print(f"Сортировка по критерию '{criteria}' выполнена")