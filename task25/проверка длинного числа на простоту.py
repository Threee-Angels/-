from math import sqrt


def is_prime(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


for j in range(10, 100):
    if is_prime(j):
        print(j)
