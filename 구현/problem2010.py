# https://www.acmicpc.net/problem/2010

n = int(input())
answer = 0
for _ in range(n) :
    answer += int(input())
print(answer - (n-1))

