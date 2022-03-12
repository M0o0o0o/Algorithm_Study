bill = [1, 5, 10, 50, 100, 500]


def solution(money, costs):
    dp = [int(1e9)] * (money + 1)
    for i in range(6):
        dp[bill[i]] = costs[i]
    for i in range(2, money+1):
        for b in range(6):
            if i - bill[b] >= 1:
                dp[i] = min(dp[i], dp[i - bill[b]] + costs[b])
    return dp[money]


# print(solution(1999, [2, 11, 20, 100, 200, 600]))


# =========================================================================

dx1, dy1 = [0, 1, 0, -1], [1, 0, -1, 0]
dx2, dy2 = [1, 0, -1, 0], [0, -1, 0, 1]
dx3, dy3 = [-1, 0, 1, 0], [0, 1, 0, -1]
dx4, dy4 = [0, -1, 0, 1], [-1, 0, 1, 0]

dx5, dy5 = [0, 1, 0, -1], [-1, 0, 1, 0]
dx6, dy6 = [1, 0, -1, 0], [0, 1, 0, -1]
dx7, dy7 = [0, -1, 0, 1], [1, 0, -1, 0]
dx8, dy8 = [-1, 0, 1, 0], [0, -1, 0, 1]


def paint(x, y, dx, dy, n, graph):
    count = [c for c in range(n-1, 0, -2)]
    if count[-1] == 2:
        count.append(1)
    num = 1
    dIndex = 0
    for c in count:
        # 각 방향마다 횟수
        for i in range(c):
            x, y = x + dx[dIndex], y + dy[dIndex]
            graph[x][y] = num
            num += 1
        dIndex += 1
        if dIndex == 4:
            dIndex = 0


def solution(n, clockwise):
    oneX, oneY = 0, -1
    twoX, twoY = -1, n-1
    threeX, threeY = n, 0
    fourX, fourY = n-1, n
    answer = [[0 for _ in range(n)] for _ in range(n)]

    if clockwise:
        paint(oneX, oneY, dx1, dy1, n, answer)
        paint(twoX, twoY, dx2, dy2, n, answer)
        paint(threeX, threeY, dx3,  dy3, n, answer)
        paint(fourX, fourY, dx4,  dy4, n, answer)

    else:
        paint(0, n, dx5, dy5, n, answer)
        paint(-1, 0, dx6, dy6, n, answer)
        paint(n-1, -1, dx7,  dy7, n, answer)
        paint(n, n-1, dx8,  dy8, n, answer)

    return answer


# # print(solution(5, True))
# print(solution(6, False))

# ====================================================

# result = 0


def dfs(node, graph, edge, visited):
    global result
    if edge > 3:
        cal = edge - 2
        result += cal * 2
    for nn in graph[node]:
        if not visited[nn]:
            visited[nn] = True
            dfs(nn, graph, edge + 1, visited)
            visited[nn] = False


def solution(n, edges):
    visited = [False for _ in range(n)]
    graph = [[] for _ in range(n)]
    for e in edges:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    for i in range(n):
        if len(graph[i]) == 1:
            visited[i] = True
            dfs(i, graph, 1, visited)
            visited[i] = False

    return result


# print(solution(5, [[0, 1], [0, 2], [1, 3], [1, 4]]))
# print(solution(4, [[2, 3], [0, 1], [1, 2]]))

dx, dy = [-1, 0], [0, 1]


def dfs(x, y, c, n, m, visited, possible, store):
    if (x, y) == (0, n):
        return 1
    for i in range(2):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx <= n and 0 <= ny <= m and not visited[c][nx][ny]:
            if store[c][nx][ny] == 0:
                visited[c][nx][ny] = True
                store[c][x][y] += dfs(nx, ny, c, n, m,
                                      visited, possible, store)
                visited[c][nx][ny] = False
            else:
                store[c][x][y] += store[c][nx][ny]
        if (x, y) in possible and c == 0:
            (mx, my) = possible[(x, y)]
            if store[1][mx][my] == 0:
                visited[1][mx][my] = True
                store[1][x][y] += dfs(mx, my, 1, n, m,
                                      visited, possible, store)
                visited[1][mx][my] = True
            else:
                store[1][x][y] += store[1][mx][my]
    return store[c][x][y]


def solution(width, height, diagonals):
    n, m = height, width
    possible = {}
    for (x, y) in diagonals:
        possible[(n-y+1, x)] = (n-y, x-1)
        possible[(n-y, x-1)] = (n-y+1, x)

    visited = [[[False for _ in range(m+1)]
                for _ in range(n+1)] for _ in range(2)]
    visited[0][n][0] = True
    store = [[[0 for _ in range(m+1)]
              for _ in range(n+1)] for _ in range(2)]
    dfs(n, 0, 0, n, m, visited, possible, store)
    print(store[0][n][0] + store[1][n][0])
    answer = 0
    return answer


solution(2, 2, [[1, 1], [2, 2]])
solution(51, 37, 	[[17, 19]])
