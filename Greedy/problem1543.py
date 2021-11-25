# https://www.acmicpc.net/problem/1543

import sys; input = sys.stdin.readline

target = input().strip('\n')
a = input().strip('\n')
index, ans = 0, 0 

while index <= len(target) - len(a): 
    if a == target[index:len(a)+index] : 
        ans += 1
        index = index + len(a)
    else :
        index += 1

print(ans)
    