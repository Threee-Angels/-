#https://inf-ege.sdamgia.ru/problem?id=13745

def check(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not((not(x <= 9) or (x * x <= a)) and (not(y * y <= a) or (y <= 9))):
                return False
    return True

for a in range(1, 1000):
    if check(a) == True:
        print(a)
