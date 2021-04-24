#https://inf-ege.sdamgia.ru/problem?id=27423
def get_count(p, n):
    cnt = 0
    s = 0
    for i in range(len(p)):
        if n - p[i] >= 0:
            cnt += 1
            n -= p[i]
            s += p[i]
        else:
            break
    return cnt, s


def get_max(cnt, s, p, n):
    now_sum = s - p[cnt - 1]
    max_val = 0
    for i in range(cnt - 1, len(p)):
        if now_sum + p[i] <= n:
            max_val = p[i]
        else:
            break
    return max_val


n, k = map(int, input().split())
p = [int(input()) for _ in range(k)]
p.sort()
cnt, s = get_count(p, n)
max_val = get_max(cnt, s, p, n)
print(cnt, max_val)
