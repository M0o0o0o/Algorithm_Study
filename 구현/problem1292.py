# https://www.acmicpc.net/problem/1292

lst = []
a, b = map(int,input().split())
answer,count = 0, 0

for i in range(1, 1001) :
    for j in range(i) :
        count += 1
        if a <= count <= b :
            answer += i

print(answer)
        
