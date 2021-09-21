# https://www.acmicpc.net/problem/1475

room = list(map(int,input()))
buf = [0] * 9
answer = 0 

for num in room :
    if num == 9 :
        buf[6] += 1
    else :
        buf[num] += 1

while True :
    if sum(buf) == 0 :
        break
    for i in range(9) :
        if buf[i] >= 1 :
            buf[i] -= 1
    if buf[6] >= 1 :
        buf[6] -= 1
    answer += 1

print(answer)
