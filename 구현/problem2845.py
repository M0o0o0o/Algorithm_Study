# https://www.acmicpc.net/problem/2845

n, m = map(int,input().split())
n *= m 
lst = list(map(int,input().split()))

for l in lst : 
    print(l - n, end = ' ')