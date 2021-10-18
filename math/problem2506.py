# https://www.acmicpc.net/problem/2506

n = int(input())
lst = list(map(int,input().split()))

count = 0
answer = 0
for l in lst :
    if not l :
        count = 0
        continue

    count += 1
    answer += count

print(answer)