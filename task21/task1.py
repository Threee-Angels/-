# https://inf-ege.sdamgia.ru/problem?id=28079
def P1(s):
    if s + 1>=24 or s + 2 >=24 or s * 2 >= 24:
        return False
    v1 = V1(s+1)
    v2 = V1(s + 2)
    v3 = V1(s * 2)
    return v1[0] and v2[0] and v3[0] and(v1[1] or v2[1] or v3[1])

def V1(s):
    if s + 1 >= 24 or s + 2 >= 24 or s * 2 >= 24:
        return [True,False]
    k = P2(s+1) or P2(s+2) or P2(s*2)
    if k:
        return [True, True]
    return [False, False]

def P2(s):
    if s + 1 >= 24 or s + 2 >= 24 or s * 2 >= 24:
        return False
    return V2(s+1) and V2(s+2) and V2(s*2)

def V2(s):
    if s + 1 >= 24 or s + 2 >= 24 or s * 2 >= 24:
        return True
    return False

for i in range(1, 23 + 1):
    if P1(i):
        print(i)
