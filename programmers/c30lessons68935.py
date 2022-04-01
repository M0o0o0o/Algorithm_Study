# https://programmers.co.kr/learn/courses/30/lessons/68935

def convert(n, q):
    base = ''
    while n > 0:
        n, mod = divmod(n, q)
        base += str(mod)
    return base[::-1]


def solution(n):
    return int(str(convert(n, 3)[::-1]), 3)


print(solution(45))

# 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력
