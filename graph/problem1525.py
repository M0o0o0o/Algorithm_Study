# # https://www.acmicpc.net/problem/1525

import sys 
input = sys.stdin.readline
from collections import deque

def bfs() :
    while q :
        node = q.popleft()
        if node == "123456780" :
            return dic[node]

        zero = node.find('0')
        x = zero // 3
        y = zero % 3
        
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < 3 and 0 <= ny < 3 :
                next = nx * 3 + ny
                nextlst = list(node)
                nextlst[zero], nextlst[next] = nextlst[next], nextlst[zero]
                nextlst = "".join(nextlst)
                
                if not dic.get(nextlst) :
                    q.append(nextlst)
                    dic[nextlst] = dic[node] + 1
                


dx, dy = [0,1,0,-1], [1,0,-1,0]

start = ""
for _ in range(3) :
    lst = input().strip()
    lst = lst.replace(' ', '')
    start += lst
    
q = deque()
q.append(start)
dic = dict()
dic[start] = 0

ans = bfs()
print(ans if ans != None else "-1")
