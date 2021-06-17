#https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=6

a = 9 ** 7 + 3 ** 21 - 8
s = ''
while a != 0:
    s += str(a % 3)
    a //= 3
print(s.count('2'))
