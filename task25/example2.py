#https://inf-ege.sdamgia.ru/problem?id=33104
from math import sqrt
n = int(sqrt(389123457))
prime = [True for _ in range(n + 1)]

for i in range(2, n + 1):
    if prime[i]:
        for j in range(i * i, n, i):
            prime[j] = False

for i in range(2, n + 1):
    if prime[i] and 289123456 <= i ** 4 <= 389123456:
        print(i ** 4,i ** 3)
