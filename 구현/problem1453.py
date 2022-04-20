# https://www.acmicpc.net/problem/1453

n = int(input())
dic = {i: False for i in range(1, 101)}
ans = 0
for l in list(map(int, input().split())):
    if not dic[l]:
        dic[l] = True
        continue
    ans += 1
print(ans)
