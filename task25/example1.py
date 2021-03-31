# https://inf-ege.sdamgia.ru/problem?id=27422
# НЕ ОПТИМАЛЬНО !!!!!!!!!

ans = []
for i in range(174457, 174505+1):
    count = 0
    delit = []
    for j in range(2, i//2+1):
        if i % j ==0:
            count+=1
            delit.append(j)
    if count == 2:
        ans.append(delit)
ans.sort(key=lambda x: x[0] * x[1])
print(ans)
