# https://www.acmicpc.net/problem/9019
from collections import deque
dp =[]

def D(num) :
    temp = num * 2
    if temp > 9999 : return temp % 10000
    return temp
def S(num) :
    if num == 0 :
        return 9999
    return num - 1
def L(num) :
    f = num % 1000
    b = num // 1000
    return f * 10 + b 
def R(num) :
    f = num % 10
    b = num // 10
    return f * 1000 + b


def bfs(start, target) :
    q = deque([(start, "")])
    dp[start] = True
    while q :
        num, com = q.popleft()
    
        if num == target :
            print(com)
            return

                
        tmp = D(num)
        if not dp[tmp] :
            q.append((tmp, com + "D"))
            dp[tmp] = True
        
        tmp = S(num)
        if not dp[tmp] :
            q.append((tmp, com + "S"))
            dp[tmp] = True

        tmp = L(num)
        if not dp[tmp] :
            q.append((tmp, com + "L"))
            dp[tmp] = True    

        tmp = R(num)
        if not dp[tmp] :
            q.append((tmp, com + "R"))
            dp[tmp] = True


        
for _ in range(int(input())) :
    start, target = map(int,input().split())
    dp =[False] * (10001)
    bfs(start, target)


