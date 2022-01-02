# https://www.acmicpc.net/problem/9094

for _ in range(int(input())) :
    n, m = map(int, input().split())
    ans = 0
    for i in range(1, n) :
        for j in range(i+1, n) :
           if (i**2 + j ** 2 + m) / (i * j) == (i**2 + j ** 2 + m) // (i * j) :
               ans += 1
    print(ans)