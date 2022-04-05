# https://programmers.co.kr/learn/courses/30/lessons/43164

from collections import defaultdict


def solution(tickets):
    answer = []
    dic = defaultdict(list)

    for ticket in tickets:
        dic[ticket[0]].append(ticket[1])

    for key in dic.keys():
        dic[key].sort(reverse=True)

    stack = ['ICN']
    while stack:
        print('--------------------')
        tmp = stack[-1]
        print('stack : ', stack)
        print('stack[-1] :', tmp)
        if not dic[tmp]:
            print('not dic [tmp] :', stack[-1])
            answer.append(stack.pop())
        else:
            print('in dic [tmp] :', dic[tmp][-1])
            stack.append(dic[tmp].pop())
        print()
        print()
        print()
    answer.reverse()

    return answer


# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], [
      "SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))

# ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
