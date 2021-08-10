# https://programmers.co.kr/learn/courses/30/lessons42587

import heapq
def solution(priorities, location):
    answer = 0 

    location_arr = [i for i in range(len(priorities))]
    index = 0
    count = 0 
    while True :
        if priorities[index] < max(priorities[index+1:]) :
            priorities.append(priorities.pop(index))
            location_arr.append(location_arr.pop(index))
        else :
            index += 1
            count += 1

        if count == len(priorities)-1 :
            break

    return location_arr.index(location) + 1

        


print(solution([1,1,9,1,1,1],0))

