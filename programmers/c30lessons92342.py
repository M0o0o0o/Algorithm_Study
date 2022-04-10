# https://programmers.co.kr/learn/courses/30/lessons/92342

diff = -1
ansBoard = []
board = [0] * 10


def dfs(arrow, idx, info):
    global diff, ansBoard, board
    if idx == 10 or arrow == 0:
        a, b = 0, 0
        for i in range(10):
            if board[i] > info[i]:
                b += i+1
            elif info[i] > board[i]:
                a += i+1
        if b-a > 0 and diff < b-a:
            diff = b-a
            ansBoard = board.copy()
        return

    if arrow >= info[idx] + 1:
        board[idx] = info[idx]+1
        dfs(arrow - (info[idx]+1), idx+1, info)
        board[idx] = 0
    dfs(arrow, idx+1, info)


def solution(n, info):
    global diff, ansBoard, board
    diff, ansBoard, board = -1, [], [0]*10
    info = info[:-1][::-1]
    dfs(n, 0, info)
    return ansBoard[::-1] + [max(n - sum(ansBoard), 0)] if diff != -1 else [-1]


print(solution(5,	[2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
print(solution(1,	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(solution(9,	[0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))
print(solution(10,	[0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))
