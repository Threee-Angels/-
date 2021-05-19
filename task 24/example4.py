#https://inf-ege.sdamgia.ru/problem?id=36037

s = input()

cnt = 3
max_cnt = 3

for i in range(3, len(s)):
    if s[i - 3] == 'X' and s[i - 2] == 'Z' and s[i - 1] == 'Z' and s[i] == 'Y':
        cnt = 3
    else:
        cnt += 1
    max_cnt = max(cnt, max_cnt)
print(max_cnt)
