#https://inf-ege.sdamgia.ru/problem?id=27421

s = input()

cnt = 1
max_cnt = 1

for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        cnt += 1
    else:
        cnt = 1
    max_cnt = max(max_cnt, cnt)
print(max_cnt)
