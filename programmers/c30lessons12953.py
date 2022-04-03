# https://programmers.co.kr/learn/courses/30/lessons/12953

def solution(arr):
    big = max(arr)
    while True:
        flag = True
        for a in arr:
            if big % a != 0:
                flag = False
                break
        
        if flag :
            return big
        big += 1
        