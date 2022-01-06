# https://www.acmicpc.net/problem/11170

for _ in range(int(input())):
    a, b= map(int, input().split())
    ans = 0
    for i in range(a, b+1) :
        ans += str(i).count('0')
    print(ans)