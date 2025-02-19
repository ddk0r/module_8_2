def personal_sum(*numbers):
    result = 0  # Инициализируем переменную для хранения суммы корректных чисел
    incorrect_data = 0  # Инициализируем счетчик некорректных данных

    # Перебираем каждый элемент в переданных аргументах
    for i in numbers:
        # Перебираем каждый элемент в текущем элементе (предполагается, что это коллекция)
        for j in i:
            try:
                result += j  # Пытаемся добавить элемент к результату
            except TypeError:
                incorrect_data += 1  # Увеличиваем счетчик некорректных данных
                print(f'некорректный тип данных для подсчета суммы - {j}')  # Выводим сообщение об ошибке

    return result, incorrect_data  # Возвращаем кортеж: сумма и количество некорректных данных


# Функция calculate_average(numbers)
# Среднее арифметическое - сумма всех данных делённая на их количество.
def calculate_average(*numbers):
    if isinstance(*numbers, int):  # Проверяем, является ли первый аргумент целым числом
        return None  # Если да, возвращаем None

    try:
        tuple_pers_sum = personal_sum(*numbers)  # Вызываем функцию personal_sum и сохраняем результат

        # Вычисляем среднее арифметическое: сумма деленная на количество корректных данных
        return tuple_pers_sum[0] / (len(*numbers) - tuple_pers_sum[1])
    except ZeroDivisionError:
        return 0  # Если происходит деление на ноль, возвращаем 0
    except TypeError:
        return f'В numbers записан некорректный тип данных'  # Обрабатываем случай некорректного типа данных


# Вывод результата
print(f'Результат 1: {calculate_average("1, 2, 3")}')
# Ожидается сообщение об ошибке, так как строка не является коллекцией чисел

print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
# Ожидается сообщение об ошибке для строк и результат среднего арифметического для чисел

print(f'Результат 3: {calculate_average(567)}')
# Ожидается None, так как передано не коллекция

print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
# Ожидается среднее арифметическое для всех чисел