# https://www.acmicpc.net/problem/9471

tc = int(input())

while tc > 0 :
    a, b = map(int,input().split())
    fibo = [0] * 500000
    fibo[1] = 1 
    for i in range(2, 500000) :
        fibo[i] = (fibo[i-1] + fibo[i-2]) % b
        if fibo[i-2] == 0  and fibo[i-1] == 1 and fibo[i] == 1 and i != 2:
            print(a, i-2)
            break

    tc -= 1