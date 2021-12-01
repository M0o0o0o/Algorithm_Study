# https://www.acmicpc.net/problem/14469

lst = []
for _ in range(int(input())) :
    a, b= map(int, input().split())
    lst.append((a,b))
lst.sort(key=lambda x:(x[0], x[1]))

time = 0 
for a,b in lst : 
    if time < a : time = a 
    time += b
print(time)