# https://www.acmicpc.net/problem/1546

n = int(input())
lst = list(map(int, input().split()))

m = max(lst) * 100
total = 0
for i in lst :
     total += (i/m)
    
print((total / n) * 10000)