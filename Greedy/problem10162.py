# https://www.acmicpc.net/problem/10162

time = int(input())
btn = [[300, 0], [60, 0], [10,0]]
possible = True

if time % 10 != 0 :
    possible = False

while possible and time > 0 :
    for i in range(len(btn)) :
        if time // btn[i][0] >= 1 :
            btn[i][1] += time // btn[i][0]
            time %= btn[i][0]

if possible :
    print(btn[0][1], btn[1][1], btn[2][1])
else :
    print(-1)
