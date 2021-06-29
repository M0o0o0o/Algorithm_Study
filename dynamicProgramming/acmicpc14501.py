# https://www.acmicpc.net/problem/14501

n = int(input())
t = []
p = []

for _ in range(n) :
    time, pay = map(int,input().split())
    t.append(time)
    p.append(pay)

result = [0] * (n+1)
value = 0

for i in range(n-1, -1, -1) :
    time = t[i] + i 

    if time <= n :
        result[i] = max(p[i] + result[time], value)
        value = result[i]        
    else :
        result[i] = value

print(value)
