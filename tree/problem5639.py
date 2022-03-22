# https://www.acmicpc.net/problem/5639

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def solution(start, end):
    if start > end:
        return

    root = lst[start]
    idx = start + 1

    while idx <= end:
        if lst[idx] > root:
            break
        idx += 1

    solution(start + 1, idx - 1)
    solution(idx, end)
    print(root)


lst = []
while True:
    try:
        lst.append(int(input()))
    except:
        break

solution(0, len(lst) - 1)

# 전위 순회: 루트 -> 왼쪽 -> 오른쪽
# 중위 순회: 왼쪽 -> 오른쪽 -> 류트
# 후위 순회: 왼쪽 -> 오른쪽 -> 루트
# 5030 24 5 28 45 98 52 60
