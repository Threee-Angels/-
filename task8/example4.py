# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=6

l = ['М', 'А', 'Г', 'И', 'С', 'Т', 'Р']
k = 0
for el1 in l:
    for el2 in l:
        for el3 in l:
            for el4 in l:
                for el5 in l:
                    s = el1 + el2 + el3 + el4 + el5
                    if s.count('М') <= 1 and s.count('А') <= 1 and s.count('Г') <= 1 and s.count('И') <= 1 and s.count('С') <= 1 and s.count('Т') <= 1 and s.count('Р') <= 1:
                        if s.count('А') == 0 and s.count('И') == 1 or  s.count('А') == 1 and s.count('И') == 0 or s.count('А') == 0 and s.count('И') == 0:
                            print(s)
                            k+=1
print(k)
