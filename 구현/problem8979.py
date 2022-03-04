# https://www.acmicpc.net/problem/8979

n, q = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

lst.sort(key=lambda x: (-x[1], -x[2], -x[3]))
for i in range(n):
    lst[i].append(''.join(map(str, lst[i][1:])))

rank, sequence_rank = 0, 0
for i in range(n):
    sequence_rank += 1
    if lst[i-1][4] != lst[i][4]:
        rank = sequence_rank

    if lst[i][0] == q:
        print(rank)
        break
