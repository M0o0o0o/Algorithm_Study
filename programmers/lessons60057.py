# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer = len(s)
    for c in range(1, (len(s)//2)+2):
        lst = list(map(''.join, zip(*[iter(s)]*c))) + ['.']
        count = 1
        zipString = 0
        for i in range(1, len(lst)):
            if lst[i-1] == lst[i]:
                count += 1
                continue
            zipString += c
            if count > 1:
                zipString += len(str(count))
            count = 1
        answer = min(answer, zipString + (len(s) % c))

    return answer


# print(solution('aabbaccc'))
# print(solution('ababcdcdababcdcd'))
# print(solution('a'))
# print(solution('abcabcdede'))
# print(solution('abcabcabcabcdededededede'))
# print(solution('ababcdcdababcdcd'))
# print(solution('ababa'))
