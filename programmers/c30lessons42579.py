# https://programmers.co.kr/learn/courses/30/lessons/42579

from audioop import reverse
from collections import defaultdict


def solution(genres, plays):
    ans = []
    dic, cnt = defaultdict(list), defaultdict(int)
    for i in range(len(genres)):
        cnt[genres[i]] += plays[i]
        dic[genres[i]].append((plays[i], i))

    for value in dic.values():
        value.sort(key=lambda x: (-x[0], x[1]))

    cnt = sorted([(cnt[key], key) for key in cnt.keys()], reverse=True)
    for c in cnt:
        ans.append(dic[c[1]][0][1])
        if len(dic[c[1]]) > 1:
            ans.append(dic[c[1]][1][1])

    return ans


print(solution(["classic", "pop", "classic",
      "classic", "pop"], [500, 600, 150, 800, 2500]))
