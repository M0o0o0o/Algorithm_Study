# https://www.acmicpc.net/problem/12782

import sys; input = sys.stdin.readline

for _ in range(int(input())) :
    ans = [0,0]
    a, b = input().strip('\n').split()
    for i in range(len(a)) :
        if a[i] != b[i] : 
            ans[int(a[i])] += 1
            
    print(max(ans[0], ans[1]))
    
    