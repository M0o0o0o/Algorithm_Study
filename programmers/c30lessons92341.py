# https://programmers.co.kr/learn/courses/30/lessons/92341

from datetime import datetime


def tollOffice(totalMin, fees):
    totalMin -= fees[0]
    if totalMin > 0:
        totalMin = (totalMin // fees[2]) + \
            (1 if totalMin % fees[2] != 0 else 0)
        return fees[1] + (totalMin * fees[3])
    else:
        return fees[1]


def timeCalculator(start, end):
    interval = list(str(datetime.strptime(
        end, "%H:%M") - datetime.strptime(start, "%H:%M")).split(":"))
    return (int(interval[0]) * 60) + int(interval[1])


def solution(fees, records):
    dic, timeStore = dict(), dict()

    for record in records:
        time, car, mode = list(record.split(' '))
        if mode == 'IN':
            dic[car] = [time, '23:59']
            continue
        dic[car][1] = time
        time = timeCalculator(dic[car][0], dic[car][1])
        dic[car] = [-1, -1]
        if car in timeStore:
            timeStore[car] += time
        else:
            timeStore[car] = time
    for key in dic.keys():
        car, start, end = key, dic[key][0], dic[key][1]
        if dic[car][0] != -1:
            time = timeCalculator(start, end)
            if car in timeStore:
                timeStore[car] += time
            else:
                timeStore[car] = time
    ans = sorted([[key, tollOffice(timeStore[key], fees)]
                 for key in timeStore.keys()], key=lambda x: x[0])
    return [a[1] for a in ans]


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
               ))

print(solution([120, 0, 60, 591],	["16:00 3961 IN", "16:00 0202 IN",
      "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]))

print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))
