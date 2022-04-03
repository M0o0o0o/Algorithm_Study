# https://programmers.co.kr/learn/courses/30/lessons/12943

def solution(num):
    cnt = 0
    while True:
        if cnt == 500:
            return -1
        if num == 1:
            return cnt
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
        cnt += 1
