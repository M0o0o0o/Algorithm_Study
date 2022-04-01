# https://programmers.co.kr/learn/courses/30/lessons/76501?language=python3


def solution(absolutes, signs):
    ans = 0
    for i in range(len(absolutes)):
        if signs[i]:
            ans += absolutes[i]
            continue
        ans += (absolutes[i] * -1)
    return ans


print(solution([4, 7, 12], [True, False, True]))
