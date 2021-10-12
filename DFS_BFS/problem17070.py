# https://www.acmicpc.net/problem/17070

n = int(input())

house = [[1] * (n + 2)]
for _ in range(n):
    house.append([1] + [int(x) for x in input().split()] + [1])
house.append([1] * (n + 2))
ways = [[[0, 0, 0] for _ in range(n + 2)] for _ in range(n + 2)]
ways[1][2][0] = 1

for c in range(3, n + 1):
    for r in range(1, n + 1):
        if house[r][c] == 0:
            ways[r][c][0] = ways[r][c - 1][0] + ways[r][c - 1][1]
            ways[r][c][2] = ways[r - 1][c][1] + ways[r - 1][c][2]

            if house[r - 1][c] == 0 and house[r][c - 1] == 0:
                ways[r][c][1] = sum(ways[r - 1][c - 1])


print(sum(ways[n][n]))                                   