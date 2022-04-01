# https://programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    for i in range(len(strings)):
        strings[i] = (strings[i][n], strings[i])
    strings.sort()
    return [string[1] for string in strings]


print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))
