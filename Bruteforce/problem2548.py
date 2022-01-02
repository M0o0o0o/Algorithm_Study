# https://www.acmicpc.net/problem/2548

n = int(input())
lst = sorted(list(map(int, input().split())))
ans, ans_total = int(1e9), int(1e9)       
for i in range(n) :
    total = 0
    for j in range(n) :
        total += abs(lst[i] - lst[j])
    if total < ans_total : 
        ans_total = total
        ans = lst[i]

print(ans)