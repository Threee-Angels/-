#https://inf-ege.sdamgia.ru/problem?id=7315


l = [0] * 100
for i in range(1, 15 + 1):
    if i == 1:
        l[i] = 1
        continue
    if i - 1 >= 1:
        l[i] += l[i - 1]
    if i % 2 == 0 and i // 2 >= 1:
        l[i] += l[i // 2]
    if i % 2 != 0 and i // 2 >= 1:
        l[i] += l[i // 2]
print(l[15])
