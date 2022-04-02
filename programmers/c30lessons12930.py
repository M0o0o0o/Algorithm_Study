# https://programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    lst = list(s.split(' '))
    for i in range(len(lst)):
        buf = list(lst[i])
        for j in range(len(buf)):
            if j % 2 == 1:
                buf[j] = buf[j].lower()
            else:
                buf[j] = buf[j].upper()
        lst[i] = ''.join(buf)
    return ' '.join(lst)


print(solution("try hello world"))
