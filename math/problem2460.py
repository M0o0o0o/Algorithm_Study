# https://www.acmicpc.net/problem/2460

ans = 0
train = 0
for _ in range(10) :
    a, b = map(int, input().split())
    train -= a 
    train += b
    ans = max(ans, train)
print(ans)