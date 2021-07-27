# https://www.acmicpc.net/problem/2581

import math

prime = [True for _ in range(10001)]

for i in range(2, int(math.sqrt(10001)) + 1) :
    if prime[i]:
  
        j = 2
        while i * j < 10001 :
            prime[i*j] = False
            j += 1 

m = int(input())
n = int(input())
total = 0
min_Value = 10001
prime[1] = False

for i in range(m, n+1) :
    if prime[i] == True :
        total += i
        min_Value = min(min_Value, i)

if total == 0 :
    print(-1)
else :
    print(total)
    print(min_Value)