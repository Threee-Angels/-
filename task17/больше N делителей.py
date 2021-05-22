#https://inf-ege.sdamgia.ru/problem?id=33762

from math import sqrt
def get_div(n):
    d = []
    for i in range(1,int(sqrt(n))+1):
        if n % i == 0 :
            d.append(i)
            if i != n // i:
                d.append(n//i)
    d.sort()
    return d

k = 0
m = 1000000
for i in range(30001, 70000+1):
    r = len(get_div(i))
    if r > 17:
        k+=1
        m = min(i, m)
print(k)
print(m)
