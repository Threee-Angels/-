#https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=7&mode=print

def F(n):
    if n > 30:
        return n*n + 5 * n + 4
    if n <= 30 and n % 2 ==0:
        return F(n+1) + 3 * F(n + 4)
    if n <= 30 and n % 2 !=0:
        return 2*F(n+2) + F(n + 5)
def sum(a):
    s = 0
    while a > 0:
        s += a % 10
        a //= 10
    return s
k = 0
for i in range(1, 1000+1):
    if sum(F(i)) == 27:
        k+=1
print(k)
