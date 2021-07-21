# https://www.acmicpc.net/problem/2108

import sys 
input = sys.stdin.readline

n = int(input())
lst = []
count = -100
frequency_arr = []
frequency = 4001
for _ in range(n) :
    lst.append(int(input()))
    
lst.sort()
for i in lst :
    if frequency != i :
        frequency_arr.append((count, frequency))
        count = 1
        frequency = i
    else :
        count += 1

frequency_arr.append((count, frequency))
frequency_arr.sort(key=lambda x:(-x[0], x[1]))

c, f = frequency_arr[0] 
if len(frequency_arr) >= 2 and frequency_arr[1][0] == c :
    f = frequency_arr[1][1]


print(round(sum(lst)/n))
print(lst[n//2])
print(f)
print(lst[n-1] - lst[0])