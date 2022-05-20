# https://programmers.co.kr/learn/courses/30/lessons/42884


def solution(routes):
    ans = 0
    routes.sort(key=lambda x: x[1])
    ll = len(routes)
    check = [0] * ll

    for i in range(ll):
        if check[i] == 0:
            time = routes[i][1]
            ans += 1
        for j in range(i+1, ll):
            if routes[j][0] <= time <= routes[j][1] and check[j] == 0:
                check[j] = 1
    return ans


def solution2(routes):
    ans = 0
    routes.sort(key=lambda x: x[1])
    time = -30001

    for r in routes:
        if time < r[0]:
            ans += 1
            time = r[1]

    return ans
