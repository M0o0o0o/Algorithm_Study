# https://programmers.co.kr/learn/courses/30/lessons/42890
from itertools import combinations


def solution(relation):
    row, col = len(relation), len(relation[0])
    ans = []
    combi = []
    for c in range(1, col + 1):
        combi.extend(combinations(range(col), c))

    for c in combi:
        flag = True
        for a in ans:
            if set(a).issubset(set(c)):
                flag = False
        search = [tuple([data[key] for key in c]) for data in relation]
        if len(set(search)) != row:
            flag = False
        if flag:
            ans.append(c)
    return len(ans)


print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], [
      "400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))
