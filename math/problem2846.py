# https://www.acmicpc.net/problem/2846

n = int(input())
lst = list(map(int, input().split())) + [-1]
cnt = 1
ans = 0
for i in range(1, n+1):
    if lst[i] > lst[i-1]:
        cnt += 1
        continue
    if cnt >= 2:
        ans = max(ans, lst[i-1] - lst[i-cnt])
    cnt = 1
print(ans)
