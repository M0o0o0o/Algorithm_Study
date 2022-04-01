# https://programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    cost = 0
    for i in range(count+1):
        cost += price * i
    return 0 if money >= cost else cost - money


print(solution(3, 20, 4))
