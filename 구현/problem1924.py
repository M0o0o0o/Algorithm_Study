# https://www.acmicpc.net/problem/1924

_m, _d = map(int,input().split())
m, d = 1, 1
one = [1, 3, 5, 7, 8, 10, 12]
zero = [4, 6, 9, 11]
day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
answer = 1
while True :
    if m == _m and d == _d :
        print(day[answer])
        break
    if (d == 30 and m in zero) or (d == 31 and m in one) or (d == 28 and m == 2) :
        m += 1
        d = 1
    else :
        d += 1

    answer += 1
    if answer == 7 : answer = 0        