# первоначальное кол-во единиц(?)

def F(s):
    while s.find('111')!=-1:
        s = s.replace ('111', '33', 1)
        s = s.replace ('333', '1', 1)
    return s
k = 0
for i in range(1, 35+1):
    s = '1' * i
    s = F(s)
    if s == '131':
        k+=1
print(k)
