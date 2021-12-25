# https://www.acmicpc.net/problem/6321

n = int(input())
lst = []
for _ in range(n) : lst.append(list(input()))
for i in range(1, n + 1) : 
    prev = lst[i-1]
    print('String #' + str(i))
    for p in prev : 
        buf = ord(p) + 1
        if buf > 90 : buf = 65 
        print(chr(buf), end = '')
    print('\n')