# https://programmers.co.kr/learn/courses/30/lessons/12901
from datetime import datetime

dateDict = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']


def solution(a, b):
    return (datetime.strptime('2016' + '-' + str(a) + '-' + str(b), '%Y-%m-%d').weekday(), dateDict[datetime.strptime('2016' + '-' + str(a) + '-' + str(b), '%Y-%m-%d').weekday()])


print(solution(5, 24))
print(solution(5, 25))
print(solution(5, 26))
print(solution(5, 27))
print(solution(5, 28))
print(solution(5, 29))
