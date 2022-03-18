# https://programmers.co.kr/learn/courses/30/lessons/77484
def solution(lottos, win_nums):
    dic = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    zero = lottos.count(0)
    hit = len(set(lottos).intersection(set(win_nums)))
    return [dic[hit + zero], dic[hit]]


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9],	[20, 9, 3, 45, 4, 35]))
