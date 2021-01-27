# https://inf-ege.sdamgia.ru/problem?id=26957
s = '>' * 1 + '1' * 26 + '2' * 10 + '3' * 14
while s.find('>1')!=-1 or s.find('>2')!=-1 or s.find('>3')!=-1:
    if s.find('>1')!=-1:
        s = s.replace('>1', '22>', 1)
    if s.find('>2')!=-1:
        s = s.replace('>2', '2>', 1)
    if s.find('>3')!=-1:
        s = s.replace('>3', '1>', 1)

print(s)

ans = 0
for el in s:
    if el != '>':
        ans += int(el)
print(ans)
