# https://www.acmicpc.net/problem/1931

n = int(input())

lst = []

for _ in range(n) :
    start, end = map(int, input().split())
    lst.append((end, start))

lst.sort()

for i in range(n) :
    end, start = lst[i][0], lst[i][1]
    lst[i] = (start, end)

result = 0 
index = 0 
currentT = -1

while index < n :
    if lst[index][0] >= currentT :
        currentT = lst[index][1]
        result += 1 
        index += 1
    else :
        index += 1

print(result)
