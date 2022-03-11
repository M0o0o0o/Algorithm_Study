# https://programmers.co.kr/learn/courses/30/lessons/17682

import sys
input = sys.stdin.readline

numList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
squaredList = {'S': 1, 'D': 2, 'T': 3}


def special(ans, d):
    if d == '*':
        if len(ans) >= 1:
            ans[-1] *= 2
        if len(ans) >= 2:
            ans[-2] *= 2
    elif d == '#' and ans:
        ans[-1] *= -1


def solution(dartResult):
    ans = []
    num = '0'
    for d in dartResult:
        if d in numList:
            num += d
            continue

        if d in squaredList:
            ans.append(int(num))
            num = ''
            ans[-1] **= squaredList[d]
            continue

        special(ans, d)
    return sum(ans)


print(solution('1S2D*3T'))
print(solution('1D2S#10S'))
print(solution('1D2S0T'))
print(solution('1S*2T*3S'))
print(solution('1D#2S*3S'))
print(solution('1T2D3D#'))
print(solution('1D2S3T*'))
