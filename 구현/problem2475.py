# https://www.acmicpc.net/problem/2475

lst = list(map(int,input().split()))
answer = 0 
for num in lst :
    answer += (num ** 2)

print(answer % 10)
