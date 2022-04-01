# https://programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    idx = len(s) // 2
    return s[idx-1] + s[idx] if len(s) % 2 == 0 else s[idx]


print(solution("abcde"))
print(solution('qwer'))
