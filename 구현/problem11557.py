# https://www.acmicpc.net/problem/11557
import sys; input = sys.stdin.readline

for _ in range(int(input())) :
    ans = ["", 0]
    for _ in range(int(input())) :
        a,b = input().split()
        if int(b) > ans[1] : 
            ans[1] = int(b) 
            ans[0] = a 
            
    print(ans[0])
        
