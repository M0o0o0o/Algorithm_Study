# https://www.acmicpc.net/problem/1806

n, s = map(int, input().split())

lst = list(map(int,input().split()))

result = int(1e9)
sum =  0
end = 0

for start in range(n) :
    while sum < s and end < n :
        sum += lst[end]
        end += 1
    
    if sum >= s and (end - start) < result :
        result = (end - start)

    sum -= lst[start]

if result == int(1e9) :
    print(0) 
else :
    print(result)

