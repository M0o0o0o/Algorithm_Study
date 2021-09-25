# https://www.acmicpc.net/problem/1977

m, n = int(input()), int(input())
answer = [0, 10001] 
for i in range(1, n) :
    num = i ** 2
    if(m <= num <= n) :
        answer[0] += num
        answer[1] = min(answer[1], num)

if answer[0] != 0 :
    print(answer[0])
    print(answer[1])
else :
    print(-1)

