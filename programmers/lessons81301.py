# https://programmers.co.kr/learn/courses/30/lessons/81301
import sys
input = sys.stdin.readline

numbers = [str(i) for i in range(10)]
engNumbers = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
              'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}


def solution(s):
    answer = ""
    index = 0
    for i in range(len(s)):
        if s[i] in numbers:
            answer += s[i]
            index = i + 1
            continue
        if s[index:i+1] in engNumbers:
            answer += engNumbers[s[index:i+1]]
            index = i + 1
            continue
    return int(answer)
