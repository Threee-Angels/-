# https://inf-ege.sdamgia.ru/problem?id=33197
def get_count(n):
    count = 0
    for i in range(1, int(n ** (1/ 2)) + 1):
        if n % i == 0 and n // i - i <= 100:
            count += 1
        if count >= 3:
            return count
    return count



for i in range(1000000, 2000000 + 1):
    if get_count(i) >= 3:
        print(i)
