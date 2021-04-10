def get_div(n):
    d = [1]
    for i in range(2, n // 2+1):
        if n % i ==0:
            d.append(i)
    d.append(n)
    return d

for i in range(312614, 312651+1):
    r = get_div(i)
    if len(r) == 6:
        print(r)
