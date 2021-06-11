#https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=7&mode=print

l = [0] * 100
for i in range(1, 15 +1):
    if i == 1:
        l[i] =1
    if i - 1 >= 1:
        l[i]+=l[i-1]
    if i - 3 >=1:
        l[i]+=l[i-3]
    if i % 2 == 0 and i // 2>= 1:
        l[i]+=l[i//2]
print(l[15])
