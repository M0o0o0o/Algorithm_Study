# https://programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    return ' '.join([buf[0].upper() + buf[1:].lower() if buf.isalpha()
                     else buf.lower() for buf in list(s.split(' '))])


print(solution("3people unFollowed me"))
