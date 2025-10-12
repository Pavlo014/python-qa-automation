# Площадь квадрата
def square(side):
    area = side * side

    # Если сторона не целое число, округляем результат вверх
    if not isinstance(side, int):
        # Округляем вверх: если есть дробная часть, добавляем 1
        area = int(area) + (1 if area > int(area) else 0)

    return int(area)  # Возвращаем целое число


print(square(5))
print(square(3.5))
print(square(4))
