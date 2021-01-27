s = '15>42>22>242>24242424>'
ans = 0
for el in s:
    if el != '>':
        ans += int(el)
print(ans)
