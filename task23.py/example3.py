#https://inf-ege.sdamgia.ru/problem?id=15807&print=true

l = [0] * 100
for i in range(3, 16+1):
    if i == 3:
        l[i] = 1
        continue
    if i - 1 >=3:
        l[i]+=l[i-1]
    if i % 2 == 0 and i // 2>=3:
        l[i]+=l[i//2]
k = l[16]
for i in range(16, 37+1):
    if i == 16:
        l[i] = k
        continue
    if i == 33:
        l[i] = 0
        continue
    if i - 1 >=16:
        l[i]+=l[i-1]
    if i % 2 == 0 and i // 2>=16:
        l[i]+=l[i//2]
print(l[37])
