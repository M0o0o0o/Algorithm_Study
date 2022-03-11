# https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0
    store = []
    for m in moves:
        pick = 0
        for row in range(len(board)):
            if 1 <= board[row][m-1] <= 100:
                pick = board[row][m-1]
                board[row][m-1] = 0
                break
        if pick == 0:
            continue
        if store and store[-1] == pick:
            store.pop()
            answer += 2
            continue
        store.append(pick)
    return answer


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [
      4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]))
