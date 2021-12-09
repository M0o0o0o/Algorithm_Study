# https://www.acmicpc.net/problem/20044

n = int(input())
lst = list(map(int, input().split()))
lst.sort()
start, end = 0, n*2-1
ans = int(1e9)
while start < end :
    ans = min(ans, lst[start] + lst[end])
    start += 1
    end -= 1
print(ans) 
    