# https://www.acmicpc.net/problem/1932

n = int(input())

tree = []

for _ in range(n):
    tree.append(list(map(int, input().split())))


result = 0
for i in range(1, n):
    for j in range(len(tree[i])):
        # dp[i][j] = dp[i][j] + max(dp[i-1][j-1]], dp[i-1][j])
        if j-1 == -1:
            left_parent = 0
        else:
            left_parent = tree[i-1][j-1]
        if j == len(tree[i-1]):
            right_parent = 0
        else:
            right_parent = tree[i-1][j]

        tree[i][j] += max(left_parent, right_parent)
        result = max(result, tree[i][j])

print(result)
