# https://www.acmicpc.net/problem/5585

coin = 1000 - int(input())
answer = 0
money = [500,100,50,10,5,1]


for m in money :
    if coin // m >= 1 :
        answer += coin // m 
        coin %= m

print(answer) 
    