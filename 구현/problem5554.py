# https://www.acmicpc.net/problem/5554

ans = 0 
for _ in range(4) :
    ans += int(input())
    
print(ans // 60)
print(ans % 60)