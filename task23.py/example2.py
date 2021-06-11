#https://inf-ege.sdamgia.ru/problem?id=16898&print=true

l = [0] * 100
for i in range(2, 14 + 1):
    if i == 2:
        l[i] = 1
    if i == 5:
        l[i] = 0
        continue
    if i == 10:
        l[i] = 0
        continue
    if i - 1 >= 2:
        l[i] += l[i - 1]
    if i % 2 == 0 and i // 2 >= 2:
        l[i] += l[i // 2]
    if i - 3 >= 2:
        l[i] += l[i - 3]
print(l[14])
