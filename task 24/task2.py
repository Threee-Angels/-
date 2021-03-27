#https://inf-ege.sdamgia.ru/problem?id=33769
s = input()
d = {}
k = []
for i in range(2, len(s)):
    if s[i-2] == s[i-1]:
        if s[i] in d.keys():
            d[s[i]]+=1
        else:
            d[s[i]] = 1
for el in d.keys():
    k.append([d[el], el])
k.sort(reverse=True)
print(k)
