# https://www.acmicpc.net/problem/2437


n = int(input())
lst = list(map(int,input().split()))
lst.sort()
answer = 1 

for l in lst : 
    if answer < l :
        break
    answer += l 

print(answer)