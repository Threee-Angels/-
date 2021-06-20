#https://inf-ege.sdamgia.ru/problem?id=33527
#1
from math import sqrt
def is_prime(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


left = 7107
right = 7141
for i in range(left, right + 1):
    if is_prime(i):
        print(i**2 * 2)

        
 ----------------------------------------------------      
 #2 (понятнее):)       
from math import sqrt
def get_div(n):
    cnt = 0
    for i in range(1, int(sqrt(n))+1):
        if n % i == 0:
            if i % 2== 0:
                cnt += 1
            if n // i != i:
                if n // i % 2 == 0:
                    cnt += 1
            if cnt > 3:
                return 4
    return cnt


for i in range(101000000, 102000000+1):
    p = get_div(i)
    if p == 3:
        print(i)

        
  
