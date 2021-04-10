#https://inf-ege.sdamgia.ru/problem?id=27850
# Решето хорошо работает на большом промежутке чисел не привыщающих 10 ** 8
from math import sqrt

k = 0
l = int(input())
r = int(input())

p = [True for i in range(r+1)]
for i in range(2, int(sqrt(r))+1):
    if p[i] == True:
        for j in range (i**2, r+1,i):
            p[j] = False
k = 1
for i in range(l,r+1):
    if p[i]==True:
        print(k,i)
    k+=1
