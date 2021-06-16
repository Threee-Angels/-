#https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=7&mode=print

p = 'ABPO'
k = 0
for el1 in p:
    for el2 in p:
        for el3 in p:
            for el4 in p:
                for el5 in p:
                    for el6 in p:
                        s = el1+el2+el3+el4+el5+el6
                        if s.count('A') == 2 and s.count('P') == 2 and s.count('B') == 1 and s.count('O') == 1:
                            if s.count('AA') == 0 and s.count('PP') == 0:
                                k+=1
print(k)
