# https://www.acmicpc.net/problem/5568
from itertools import combinations
import sys 
input = sys.stdin.readline

n, k = int(input()), int(input())
ans = set()

def recur(index, make, lst) :
    global ans
    if len(make) == k : 
        if "".join(make) not in ans : 
            ans.add("".join(make))
        return
    for i in range(len(lst)) : 
        if i not in index : 
            recur([i] + index, make + [lst[i]], lst)
    return 

LST = [] 
for _ in range(n) :
    LST.append(input().strip('\n'))

for c in list(combinations(LST, k)) : 
    recur([], [], list(c))

print(len(ans))

