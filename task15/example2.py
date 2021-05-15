#https://inf-ege.sdamgia.ru/problem?id=8106

def check(a):
    for x in range(1, 10000):
        if not(x % a == 0 or x % 6 != 0 or x % 4 != 0):
            return False
    return True

for a in range(1, 10000):
    if check(a) == True:
        print(a)
