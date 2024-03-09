import math


def square():
    s = float(input("Введи число: "))
    s = math.ceil(s * s)
    print("Площадь квадрата равна:", s)


square()
