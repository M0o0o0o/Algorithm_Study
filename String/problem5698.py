# https://www.acmicpc.net/problem/5698

while True:
    s = list(input().split(' '))
    if s[0] == '*':
        break
    ans = 'Y'
    for i in range(1, len(s)):
        if s[i-1][0].upper() != s[i][0].upper():
            ans = 'N'
    print(ans)
