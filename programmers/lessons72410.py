# https://programmers.co.kr/learn/courses/30/lessons/72410

import sys
input = sys.stdin.readline

etc = ['-', '_', '.'] + [str(num) for num in range(10)] + \
    [chr(alpha) for alpha in range(97, 123)]


def remove(new_id):
    return ''.join([s if s in etc else "" for s in new_id])


def rmFirstDot(new_id):
    if new_id and new_id[0] == '.':
        new_id = new_id[1:]
    return new_id


def rmLastDot(new_id):
    if new_id and new_id[-1] == '.':
        new_id = new_id[:len(new_id)-1]
    return new_id


def rmDots(new_id):
    if len(new_id) == 0:
        return new_id

    returnString, dotCount = new_id[0], 0
    if new_id[0] == '.':
        dotCount = 1
        returnString = ""
    for i in range(1, len(new_id)):
        if new_id[i] == '.':
            dotCount += 1
            continue
        if dotCount >= 2:
            returnString += '.'
        else:
            returnString += '.' * dotCount
        dotCount = 0
        returnString += new_id[i]
    return returnString


def solution(new_id):
    new_id = new_id.lower()
    new_id = remove(new_id)
    new_id = rmDots(new_id)
    new_id = rmFirstDot(new_id)
    new_id = rmLastDot(new_id)
    new_id = 'a' if len(new_id) == 0 else new_id
    new_id = new_id[:15] if len(new_id) >= 16 else new_id
    new_id = rmLastDot(new_id)
    new_id = new_id + (new_id[-1] * (3 - len(new_id))
                       ) if len(new_id) < 3 else new_id
    return new_id


print(solution("...!@BaT#*..y.abcdefghijklm") == "bat.y.abcdefghi")
print(solution("z-+.^.") == "z--")
print(solution("=.=") == "aaa")
print(solution("123_.def") == "123_.def")
print(solution("abcdefghijklmn.p") == "abcdefghijklmn")
