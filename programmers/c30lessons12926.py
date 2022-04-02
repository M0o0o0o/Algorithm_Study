# https://programmers.co.kr/learn/courses/30/lessons/12926

def convert(alpha, n):
    num = ord(alpha) + n
    print(alpha, num)
    return chr(num - 26) if (alpha.islower() and num > 122) or (alpha.isupper() and num > 90) else chr(num)


def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isalpha():
            s[i] = convert(s[i], n)
    return ''.join(s)


print(solution("a B z", 4))
print(solution("AB", 1))
