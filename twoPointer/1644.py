# https://www.acmicpc.net/problem/1644

import math

n = int(input())
arr = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n)) + 1) :
    if arr[i] == True :
        j = 2
        while i * j <= n :
            arr[i*j] = False
            j += 1

prime = []

for i in range(2, n+1) :
    if arr[i] :
        prime.append(i)

result = 0
end = 0
sum = 0
for start in range(len(prime)) :
    while sum < n and end < len(prime) :
        sum += prime[end]
        end += 1

    if sum == n :
        result += 1

    sum -= prime[start]

print(result)

