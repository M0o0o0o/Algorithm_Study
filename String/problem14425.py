# https://www.acmicpc.net/problem/14425

import sys 
input = sys.stdin.readline

n, m = map(int, input().split())
dic = dict()
ans = 0

for _ in range(n) :
    dic[input().strip('\n')] = True

for _ in range(m) :
    if dic.get(input().strip('\n')) :
        ans += 1

print(ans)