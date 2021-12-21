# https://www.acmicpc.net/problem/1652

n = int(input())
room = []
for _ in range(n) :
    room.append(list(input().strip('\n')))
ans = [0,0]
for i in range(n) :
    count = 0 
    for j in range(n) :
        if room[i][j] == '.' : count += 1
        elif room[i][j] == 'X' : 
            if count >= 2 : 
                ans[0] += 1
            count = 0
    if count >= 2 : ans[0] += 1

for i in range(n) :
    count = 0 
    for j in range(n) :
        if room[j][i] == '.' : count += 1
        elif room[j][i] == 'X' : 
            if count >= 2 : 
                ans[1] += 1
            count = 0
    if count >= 2 : ans[1] += 1
print(ans[0], ans[1])