# https://www.acmicpc.net/problem/2502

d, k = map(int, input().split())
ans = [0,0]
for a in range(1,k) :
    if sum(ans) != 0 : break
    for b in range(1,k) :
        prev_, next_ = a, b
        for c in range(3, d+1) : 
            prev_, next_  = next_, prev_ + next_
        if next_ == k : 
            ans = [a,b]
            break    
        
print(ans[0])
print(ans[1])