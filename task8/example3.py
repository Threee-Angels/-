#https://inf-ege.sdamgia.ru/problem?id=13486&print=true


l = ['A', 'B', 'C', 'X']
k = 0
for el1 in l:
    for el2 in l:
        for el3 in l:
            for el4 in l:
                for el5 in l:
                    s = el1 + el2 + el3 + el4 + el5
                    if s.count('X') == 1:
                        if el1==('X') or el5 ==('X'):
                            if el2!=('X') and el3!=('X') and el4!=('X'):
                                print(s)
                                k+=1
print(k)
