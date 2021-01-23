# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=6&mode=print
# задание 2

def F(x, y, z, w):
    return int((x and (not y)) or (y == z) or w)

p = [0, 1]
for x in p:
    for y in p:
        for z in p:
            for w in p:
                k = F(x, y, z, w)
                print(x, y, z, w, k)
