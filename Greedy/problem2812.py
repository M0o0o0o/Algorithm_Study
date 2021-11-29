# https://www.acmicpc.net/problem/2812
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(input().strip('\n'))
ans = []
bufK = k
for i in range(n) :
    while bufK and ans : 
        if ans[-1] < lst[i] : 
            ans.pop()
            bufK -= 1
            continue
        break
    ans.append(lst[i])
    
print("".join(ans[:n-k]))

