
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

lst = [int(input()) for _ in range(n)]
votes = [0] * n
for _ in range(m):
    vote = int(input())
    for i in range(n):
        if lst[i] <= vote:
            votes[i] += 1
            break

print(votes.index(max(votes))+1)

# i번째 재밌는 경기에 개최 비용
