# https://www.acmicpc.net/problem/1271

n, m = map(int, input().split())
ans = 0

while True :
    if n // m > 0 :
        ans += n // m 
        n %= m 
    else : break

print(ans)
print(n)