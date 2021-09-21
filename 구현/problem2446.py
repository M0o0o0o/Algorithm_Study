# https://www.acmicpc.net/problem/2446

n = int(input())
star = (2 * n) - 1 
current = star
for _ in range(n) :
    for _ in range((star - current) // 2) :
        print(' ', end = '')
    for i in range(current) :
        print('*', end = '')
    current -= 2
    print("")

current += 4 
for _ in range(1, n) :
    for _ in range((star - current) // 2) :
        print(' ', end = '')
    for i in range(current) :
        print('*', end = '')
    current += 2
    print("")
