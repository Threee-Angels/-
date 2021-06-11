#https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=7&mode=print

l = ['A', 'B', 'P', 'O', 'P', 'A']
k = 0
ans = set()
for el1 in l:
    for el2 in l:
        for el3 in l:
            for el4 in l:
                for el5 in l:
                    for el6 in l:
                        s = el1 + el2 + el3 + el4 + el5 + el6
                        if s.count('A') == 2 and s.count('P') == 2 and s.count('B') == 1 and s.count('O') == 1:
                            if s.count('AA') == 0 and s.count('PP') == 0:
                                ans.add(s)
                                k += 1
print(len(ans))
