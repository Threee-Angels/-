#https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=6&mode=print
# задание 22

k = 0
for i in  range(0, 1000000):
    x = i
    a = 0
    b = 0
    while x > 0:
      a = a + 1
      b = b + (x % 10)
      x = x // 10
    if a == 2 and b == 12:
        k+=1
        print(i)
print(k)
