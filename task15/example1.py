#https://inf-ege.sdamgia.ru/problem?id=9804

def check(a):
    for x in range(1, 10000):
        if not(x & 29 == 0 or x & 17 != 0 or x & a != 0):
            return False
    return True


for a in range(1, 1000):
    if check(a) == True:
        print(a)
        break
