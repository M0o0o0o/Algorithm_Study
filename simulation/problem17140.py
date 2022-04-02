# https://www.acmicpc.net/problem/17140

r, c, k = map(int, input().split())
row, col = 3, 3

# 행 또는 열의 크기가 100을 넘어가는 경우에는 처음 100개를 제외한 나머지를 버린다.
# 한 행 또는 한 열에 있는 수를 정렬하려면, 각각의 수가 몇 번 나왔는지 알아야 한다.
# 그 다음, 수의 등장 횟수가 커지는 순으로,
# 그러한 것이 여러가지면, 수가 커지는 것으로 정렬한다. 그 다음에는
# 배열 A에 정렬된 결과를 다시 넣어야 한다.
# 정렬된 결과를 배열에 넣을 때는, 수와 등장 횟수를 모두 넣으며, 순서는 수가 먼저이다.
board = [[0 for _ in range(101)]for _ in range(101)]
for i in range(1, 4):
    buf = [0] + list(map(int, input().split()))
    for j in range(1, 4):
        board[i][j] = buf[j]

ans = 0
while board[r][c] != k:
    ans += 1
    if row >= col:  # 행 연산
        # 행 연산하면서 열 크기가 커지니 col을 업데이트하면서 처리
        for i in range(1, row+1):
            dic = dict()
            for j in range(1, col+1):
                if board[i][j] == 0:
                    break
                if board[i][j] not in dic:
                    dic[board[i][j]] = 1
                else:
                    dic[board[i][j]] += 1
            newLst = sorted([(key, dic[key])
                            for key in dic.keys()], key=lambda x: (x[1], x[0]))

            index = 1
            for node in newLst:
                board[i][index], board[i][index+1] = node
                index += 2
            col = max(col, len(newLst) * 2)
        continue
    for i in range(1, col+1):
        dic = dict()
        for j in range(1, row+1):
            if board[j][i] == 0:
                break
            if board[j][i] not in dic:
                dic[board[j][i]] = 1
            else:
                dic[board[j][i]] += 1
            newLst = sorted([(key, dic[key])
                            for key in dic.keys()], key=lambda x: (x[1], x[0]))
            index = 1
            for node in newLst:
                board[index][i], board[index+1][i] = node
                index += 2
            row = max(row, len(newLst) * 2)

            # 열 연산
            # 열 연산하면서 행 크기가 커지니 row를 업데이트하면서 처리
    row = min(row, 100)
    col = min(col, 100)

print(ans)
