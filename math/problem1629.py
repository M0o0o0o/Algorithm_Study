# https://www.acmicpc.net/problem/1629

a, b, c = list(map(int, input().split()))


def cal(cnt):
    if cnt == 1:
        return a % c
    if cnt % 2 == 0:
        left = cal(cnt // 2)
        return left * left % c
    else:
        left = cal(cnt // 2)
        return left * left * a % c


print(cal(b))
