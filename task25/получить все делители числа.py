from math import sqrt


def get_divisor(n):
    # число делителей без учётна 1 и самого числа
    d = []
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            d.append(i)
    return d


for i in range(210235, 210300+1):
    t = get_divisor(i)
    if len(t) == 4:
        print(t)
