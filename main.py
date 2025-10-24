import math


def solve(a: float, b: float, c: float) -> list:
    epsilon = 1e-10

    if abs(a) < epsilon:
        raise ValueError(f'Коэффициент "a" не может быть равен 0 или меньше {epsilon}')

    D = b ** 2 - 4 * a * c

    if D < 0:
        return []

    elif abs(D) < epsilon:
        x = -b / 2 * a
        return [x, x]

    else:
        return [(-b + math.sqrt(D)) / 2 * a, (-b - math.sqrt(D)) / 2 * a]
