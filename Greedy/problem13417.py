# https://www.acmicpc.net/problem/13417

for _ in range(int(input())) :
    n = int(input())
    lst = list(input().split())
    ans = lst[0]
    for i in range(1, n) :
        if lst[i] > ans[0] : 
            ans += lst[i]
        else :
            ans = lst[i] + ans
    print(ans)    