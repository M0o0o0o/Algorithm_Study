# https://www.acmicpc.net/problem/5597

check = set([i for i in range(1, 31)])
papers = set([int(input()) for _ in range(28)])
ans = list(check - papers)
for i in sorted(ans):
    print(i)
