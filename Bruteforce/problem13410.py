# https://www.acmicpc.net/problem/13410

n, k = map(int, input().split())
ans = 0
for i in range(k+1) :
    ans = max(ans, int(str(n * i)[::-1]))
print(ans)