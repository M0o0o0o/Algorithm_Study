# https://programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations


def solution(orders, course):
    dic = {c: set() for c in course}
    dicCnt = {c: 0 for c in course}
    for c in course:
        for i in range(len(orders)):
            combis = list(combinations(list(orders[i]), c))
            for combi in combis:
                combi = tuple(sorted(list(combi)))
                if dic[c] in combi:
                    continue
                cnt = 0
                for j in range(len(orders)):
                    if set(combi).issubset(set(orders[j])):
                        cnt += 1
                if cnt < 2:
                    continue
                if cnt > dicCnt[c]:
                    dic[c] = set([combi])
                    dicCnt[c] = cnt
                elif cnt == dicCnt[c]:
                    dic[c].add(combi)
    ans = []
    for c in course:
        for menu in list(dic[c]):
            ans.append(''.join(sorted(''.join(list(menu)))))
    return sorted(ans)


# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],	[2s, 3, 4]))
# print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"],	[2, 3, 4]))
