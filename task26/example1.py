#https://inf-ege.sdamgia.ru/problem?id=27423
def get_count(p, n):
    #p - список всех файлов
    #n - максимальный объём
    cnt = 0
    for i in range(len(p)):
        if n - p[i] >= 0:
            cnt +=1
            n -= p[i]
        else:
            break
    return cnt


def get_max(cnt, n, p):
    max_val = 0
    now_sum = sum(p[:cnt-1])
    for i in range(cnt - 1, len(p)):
        if now_sum + p[i] <=n:
            max_val = p[i]
        else:
            break
    return max_val


n, k = map(int, input().split())
p = [int(input()) for i in range(k)]
p.sort()
cnt = get_count(p,n)
max_val= get_max(cnt, n, p)
print(cnt, max_val)
