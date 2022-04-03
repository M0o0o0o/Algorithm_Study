# https://programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    return True if x % sum(list(map(int, str(x)))) == 0 else False
