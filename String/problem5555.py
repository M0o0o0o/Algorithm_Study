# https://www.acmicpc.net/problem/5555
import sys 
input = sys.stdin.readline

f = input().strip('\n')
ans = 0
for _ in range(int(input())): 
    if (input().strip('\n') * 2).find(f) != -1 : ans += 1
    
print(ans)