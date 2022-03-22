# https://www.acmicpc.net/problem/2263
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


# inorder : 5 24 28 30 45 50 52 60 98 (왼쪽 -> 루트 -> 오른쪽)
# postorder : 5 28 24 45 30 60 52 98 50 (왼쪽 -> 오른쪽 -> 루트)
# proorder : 50 30 24 5 28 45 98 52 60

def preorder(istart, iend, pstart, pend):
    if istart > iend:
        return

    root = postorder[pend]
    idx = dic[root]
    leftCnt = idx - istart

    print(root, end=' ')
    preorder(istart, idx-1, pstart, pstart+leftCnt-1)
    preorder(idx+1, iend, pstart+leftCnt, pend-1)


n = int(input())
ans = []
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
dic = {inorder[i]: i for i in range(n)}
preorder(0, n-1, 0, n-1)
