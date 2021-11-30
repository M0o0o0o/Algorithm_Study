# https://www.acmicpc.net/problem/16435
import sys; input = sys.stdin.readline

n, height = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

for l in lst : 
    if height >= l : height += 1
    else : break

print(height)