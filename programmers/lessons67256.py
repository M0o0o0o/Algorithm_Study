# https://programmers.co.kr/learn/courses/30/lessons/67256

import sys
input = sys.stdin.readline

leftOnly = [1, 4, 7]
rightOnly = [3, 6, 9]
keyMapping = {1: (0, 0), 2: (0, 1), 3: (0, 2),
              4: (1, 0), 5: (1, 1), 6: (1, 2),
              7: (2, 0), 8: (2, 1), 9: (2, 2),
              '*': (3, 0), 0: (3, 1), '#': (3, 2)}


def calc(n, leftPos, rightPos, hand):
    nx, ny = keyMapping[n]
    lx, ly = keyMapping[leftPos]
    rx, ry = keyMapping[rightPos]
    leftMov = abs(nx - lx) + abs(ny - ly)
    rightMov = abs(nx - rx) + abs(ny - ry)
    if leftMov == rightMov:
        return hand[0].upper()
    return 'L' if leftMov < rightMov else 'R'


def solution(numbers, hand):
    answer = ''
    leftPos, rightPos = '*', '#'
    for n in numbers:
        if n in leftOnly:
            answer += 'L'
            leftPos = n
            continue
        if n in rightOnly:
            answer += 'R'
            rightPos = n
            continue
        winHand = calc(n, leftPos, rightPos, hand)
        answer += winHand
        if winHand == 'R':
            rightPos = n
        else:
            leftPos = n
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right') == "LRLLLRLLRRL")
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left') == "LRLLRRLLLRR")
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right') == "LLRLLRLLRL")
