# https://www.acmicpc.net/problem/3273

n = int(input())
lst = list(map(int, input().split()))
target = int(input())

lst.sort()

count = 0
start = 0
end = n-1

while True :
    if start >= end :
        break
    total = lst[start] + lst[end] 
    
    if total == target : 
        count += 1 
        start += 1
        end -= 1
    elif total > target :
        end -= 1
    else :
        start += 1

print(count)