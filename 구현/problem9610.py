# https://www.acmicpc.net/problem/9610
import sys; input = sys.stdin.readline

ans = [0] * 5
for _ in range(int(input())) :
    x, y = map(int, input().split())
    if x == 0 or y == 0 :
        ans[0] += 1
        continue
    if x > 0 and y > 0 : ans[1] += 1
    elif x > 0 and y < 0 : ans[4] += 1
    elif x < 0 and y > 0 : ans[2] += 1
    else : ans[3] += 1
    
for i in range(1, 5) :
    print('Q' + str(i) + ":", ans[i])
    
print('AXIS:', ans[0])
    
     

    