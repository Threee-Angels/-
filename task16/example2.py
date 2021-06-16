#https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=7&mode=print

def good(a):
    k = 0
    s = str(a)
    for el in s:
        k += int(el)
    return k


def F(n):
    if n > 30:
        return n * n + 5 * n + 4
    if n <= 30 and n % 2 == 0:
        return F(n + 1) + 3 * F(n + 4)
    if n <= 30 and n % 2 != 0:
        return 2 * F(n + 2) + F(n + 5)


k = 0

for i in range(1, 1000 + 1):
    g = good(F(i))
    if g == 27:
        k += 1
print(k)
