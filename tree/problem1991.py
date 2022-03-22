# https://www.acmicpc.net/problem/1991
import sys

input = sys.stdin.readline
n = int(input())
tree = dict()
preAns, inAns, postAns = [], [], []


def dfs(node):
    preAns.append(node)
    for i in range(2):
        if tree[node][i] != '.':
            dfs(tree[node][i])
        if i == 0:
            inAns.append(node)
    postAns.append(node)


for _ in range(n):
    a, b, c = list(input().strip('\n').split(' '))
    tree[a] = [b, c]

dfs('A')

print(''.join(preAns))
print(''.join(inAns))
print(''.join(postAns))
