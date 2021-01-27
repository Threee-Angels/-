# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=11

def F(n):
    if n > 25:
        return 2*n**3 + 1
    if n<= 25:
        return F(n+2) + 2 * F(n+3)

k = 0
for i in range (1, 1000+1):
    if F(i) % 11 == 0:
        k+=1
print(k)


