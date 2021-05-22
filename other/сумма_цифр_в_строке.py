s = input()
k = 0
for el in s:
    if el.isdigit():
        k += int(el)
print(k)
