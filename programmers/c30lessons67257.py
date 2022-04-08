# https://programmers.co.kr/learn/courses/30/lessons/67257?language=python

from itertools import permutations


def calc(ex, OP):
    lst = []
    num = ''
    for i in range(len(ex)):
        if ex[i].isdigit():
            num += ex[i]
            continue
        lst.append(num)
        num = ''
        lst.append(ex[i])
    lst.append(num)
    for i in range(2):
        op = OP[i]
        while lst.count(op) > 0:
            opIdx = lst.index(op)
            left, right = lst[opIdx-1], lst[opIdx+1]
            lst = lst[:opIdx-1] + \
                ['(' + left + op + right + ')'] + lst[opIdx+2:]
    return eval(''.join(lst))


def solution(expression):
    ans = 0
    op = list(permutations(['*', '+', '-'], 3))
    for o in op:
        ans = max(ans, abs(calc(expression, o)))
    return ans


print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))

# print(solution("50+1-4"))
# print(solution("2-990-5+2"))
