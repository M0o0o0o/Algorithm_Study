# https://www.acmicpc.net/problem/1547

ans = 1
for _ in range(int(input())) :
    a, b = map(int, input().split())
    if ans in [a, b] : 
        if ans == a : ans = b 
        else : ans = a
        
print(ans)