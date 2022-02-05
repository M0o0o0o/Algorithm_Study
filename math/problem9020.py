# https://www.acmicpc.net/problem/9020
prime = [0 for i in range(10001)]
prime[1] = 1
for i in range(2, 98):
    for j in range(i * 2, 10001, i):
        prime[j] = 1
t = int(input())
for i in range(t):
    a = int(input())
    b = a // 2
    for j in range(b, 1, -1):
        if prime[a - j] == 0 and prime[j] == 0:
            print(j, a - j)
            break
