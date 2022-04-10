# https://programmers.co.kr/learn/courses/30/lessons/72412

from collections import defaultdict
from itertools import combinations
from bisect import bisect_left


def solution(infos, queries):
    ans = []
    dic = defaultdict(list)
    for info in infos:
        info = info.split()
        condition = info[:-1]
        score = int(info[-1])
        for i in range(5):
            case = list(combinations([0, 1, 2, 3], i))
            for c in case:
                temp = condition.copy()
                for idx in c:
                    temp[idx] = '-'
                key = ''.join(temp)
                dic[key].append(score)
    for key in dic.keys():
        dic[key].sort()

    for query in queries:
        query = query.replace("and ", "")
        query = query.split()
        key = ''.join(query[:-1])
        score = int(query[-1])
        count = 0
        if key in dic:
            lst = dic[key]
            idx = bisect_left(lst, score)
            count = len(lst) - idx
        ans.append(count)
    return ans


print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
      ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))
