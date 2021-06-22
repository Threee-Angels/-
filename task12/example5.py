#https://inf-ege.sdamgia.ru/problem?id=33487

k = 0
m = 1000000
for el in range(22000, 33000 + 1):
    kd = 0
    if el % 11 == 0:
        kd += 1
    if el % 13 == 0:
        kd += 1
    if el % 17 == 0:
        kd += 1
    if el % 19 == 0:
        kd += 1
    if kd == 2:
        k += 1
        m = min(el, m)
print(k)
print(m)
