# https://www.acmicpc.net/problem/19539

n = int(input())
buf = [0] * 2 
apple = list(map(int,input().split()))
for i in apple : 
    buf[0] += i 
    buf[1] += i // 2

if buf[0] % 3 == 0 and (buf[0] / 3) <= buf[1] :
    print('YES')
else :
    print('NO')


    