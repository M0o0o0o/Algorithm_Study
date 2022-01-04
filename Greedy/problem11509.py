# https://www.acmicpc.net/problem/11509

n = int(input())
lst = list(map(int, input().split()))
ans = 0
for i in range(n) :
    if lst[i] == -1 : continue
    arrow = lst[i] -1 
    lst[i] = -1 
    ans += 1
    for j in range(i+1, n) :
        if lst[j] == arrow : 
            arrow -= 1
            lst[j] = -1
            
        
print(ans)
