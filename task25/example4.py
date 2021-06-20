# https://inf-ege.sdamgia.ru/problem?id=27857
from math import sqrt
def get_div(n):
    p = []
    for i in range(1, int(sqrt(n))+1):
        if n % i == 0:
            p.append(i)
            if i != n // i:
                p.append(n // i)
    return len(p)

max_k = 0
ans = []
for i in range(84052,84130+1):
    k = get_div(i)
    if k > max_k:
        max_k = k
        ans = [k, i]
print(ans)
