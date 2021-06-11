#https://inf-ege.sdamgia.ru/problem?id=10290&print=true

s = '1' + '8' * 80
while s.find('18')!= -1 or s.find('288') != -1 or s.find('3888')!= -1:
    if s.find('18')!=-1:
        s = s.replace('18', '2', 1)
    elif s.find('288') != -1:
        s = s.replace('288', '3', 1)
    else:
        s =s.replace('3888', '1', 1)
print(s)
