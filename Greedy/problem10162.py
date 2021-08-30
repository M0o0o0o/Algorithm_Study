# https://www.acmicpc.net/problem/10162

time = int(input())
btn = [300,60,10]

if time % 10 != 0 :
    print(-1)
else :
    for i in range(len(btn)) :
        if time // btn[i] >= 1 :
            print(time // btn[i], end = ' ')
            time %= btn[i]
        else :
            print(0, end = ' ')
