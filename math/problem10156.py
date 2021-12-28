# https://www.acmicpc.net/problem/10156

n, m, k = map(int, input().split())
if n*m-k > 0:
    print(n * m - k) 
elif n*m-k <= 0 : print(0)
