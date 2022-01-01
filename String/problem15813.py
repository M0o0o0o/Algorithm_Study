# https://www.acmicpc.net/problem/15813

n = int(input())
ans = 0
for s in input() :
   ans += ord(s) - 64
   
print(ans) 