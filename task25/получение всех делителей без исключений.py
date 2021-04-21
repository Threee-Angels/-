#https://inf-ege.sdamgia.ru/problem?id=27853
from math import sqrt
def get_div(n):
    d =[]
    for i in range(1, int(sqrt(n))+1):
        if n % i ==0:
            if i % 2 ==0:
                d.append(i)
            if n // i % 2 == 0:
                d.append(n//i)
    d.sort()
    return d

for i in range(125256,125330+1):
    r = get_div(i)
    if len(r) == 6:
        print(r)
