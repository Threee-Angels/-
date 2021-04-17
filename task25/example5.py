# https://inf-ege.sdamgia.ru/problem?id=29673
from math import sqrt
def is_prime(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i ==0:
            return False
    return True
# 106 - 122

k = 0
for  i in range(106, 122 + 1):
    if is_prime(i):
        print(i ** 4, i ** 3)
