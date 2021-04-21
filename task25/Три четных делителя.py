#https://inf-ege.sdamgia.ru/problem?id=33527
from math import sqrt
def is_prime(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


left = 7107
right = 7141
for i in range(left, right + 1):
    if is_prime(i):
        print(i**2 * 2)
