# https://www.acmicpc.net/problem/2702

for _ in range(int(input())) :
    a,b = map(int, input().split()) 
    ans = [0,0]
    
    d = 2
    while True : 
        if d % a == 0 and d % b == 0 : 
            ans[0] = d 
            break
        d += 1
    
    for d in range(1, min(a,b) + 1) : 
        if a % d == 0 and b % d == 0 : 
            ans[1] = d
    
    print(ans[0], ans[1])