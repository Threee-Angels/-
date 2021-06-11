# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=11
# если условие задачи про исключение двух подряд букв в слове
l = ('А', 'Б', 'А', 'К')
k = 0
ans = set()
for el1 in l:
    for el2 in l:
        for el3 in l:
            for el4 in l:
                s = el1 + el2 + el3 + el4
                if s.count('А') == 2 and s.count('Б') == 1 and s.count('К') == 1:
                    if s.count('АА') == 0:
                        ans.add(s)
                        k+=1
print(len(ans))
