#https://inf-ege.sdamgia.ru/problem?id=10321

p = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}

inf = set(range(-10000, 100000))
not_p = inf.difference(p)
not_q = inf.difference(q)
not_p_plus_not_q = not_p.union(not_q)
print(inf.difference(not_p_plus_not_q))
