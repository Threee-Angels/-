from math import sqrt
n = 1000000
prime = [True for _ in range(n)]

for i in range(2, int(sqrt(n)) + 1):
    if prime[i]:
        for j in range(i * i, n, i):
            prime[j] = False
print(prime[])
