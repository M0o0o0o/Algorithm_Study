# https://www.acmicpc.net/problem/11367

def cal(score):
    if 0 <= score <= 59:
        return 'F'
    elif 60 <= score <= 66:
        return 'D'
    elif 67 <= score <= 69:
        return 'D+'
    elif 70 <= score <= 76:
        return 'C'
    elif 77 <= score <= 79:
        return 'C+'
    elif 80 <= score <= 86:
        return 'B'
    elif 87 <= score <= 89:
        return 'B+'
    elif 90 <= score <= 96:
        return 'A'
    else:
        return 'A+'


for _ in range(int(input())):
    lst = list(input().split(' '))
    print(lst[0], cal(int(lst[1])))
