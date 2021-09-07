# https://www.acmicpc.net/problem/2747

n = int(input())
fibo = [0] * (1500001)
fibo[1] = 1 
for i in range(2, 1500001) :
    fibo[i] = (fibo[i-1] + fibo[i-2]) % 1000000
print(fibo[n % 1500000] )

