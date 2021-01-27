# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=11
k = 0
for i in range(101, 1000000):
    x = i
    L = x - 30
    M = x + 30
    while L != M:
      if L > M:
        L = L - M
      else:
        M = M - L
    if M == 15:
        print(i)
print(k)
