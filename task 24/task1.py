# https://inf-ege.sdamgia.ru/problem?id=33103
count = 0
with open('data.txt') as file:
    while True:
        line = file.readline()
        if line:
            if line.count('A') > line.count('E'):
                count+=1
        else:
            break
print(count)
