# https://www.acmicpc.net/problem/16500
import sys


def solution(index):
    if index == len(S):
        dp[-1] = 1
        return
    else:
        if dp[index] != 1:
            dp[index] = 1

            for i in range(N):
                if len(S[index:]) >= len(A[i]):
                    for j in range(len(A[i])):
                        if S[index+j] != A[i][j]:
                            t = False
                            break

                    else:
                        solution(index + len(A[i]))


S = sys.stdin.readline().strip()
N = int(sys.stdin.readline())
A = []

for i in range(N):
    A.append(sys.stdin.readline().strip())

dp = [0] * (len(S) + 1)
solution(0)

print(dp[-1])
