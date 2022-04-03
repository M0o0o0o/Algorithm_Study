# https://programmers.co.kr/learn/courses/30/lessons/12940

def solution(n, m):
    small, big = min(n, m), max(n, m)
    ans = [-1, -1]
    # 최대 공약수, 최소 공약수 반환
    for i in range(small, -1, -1):
        if small % i == 0 and big % i == 0:
            ans[0] = i
            break
    num = big
    while True:
        if num % big == 0 and num % small == 0:
            ans[1] = num
            break
        num += 1
    return ans
