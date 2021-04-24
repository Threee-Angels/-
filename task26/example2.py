# https://inf-ege.sdamgia.ru/problem?id=29674
from math import ceil


def get_pos(p):
    for i in range(len(p)):
        if p[i] > 50:
            return i
    print('ДЛЯ СЕБЯ:)')


n = int(input())
p = [int(input()) for _ in range(n)]
p.sort()
k = get_pos(p)
ans = sum(p[:k])
sale_cnt = (len(p) - k) // 2
ans2 = ceil(float(sum(p[k:k+sale_cnt])) * 0.75)
ans3 = sum(p[k+sale_cnt:])
print(ans + ans2 + ans3, p[k+sale_cnt - 1])
