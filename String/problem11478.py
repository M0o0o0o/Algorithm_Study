# https://www.acmicpc.net/problem/11478

s = input()
ans = set()
count = 1

for c in range(len(s)):
    for i in range(c, len(s)):
        ans.add(s[i-c:i+1])

print(len(ans))
