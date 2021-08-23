# https://programmers.co.kr/learn/courses/30/lessons/42583
 
from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    index = 0
    total_weight = 0
    q = deque([])
    while True :
        for i in range(len(q)) :
            q[i] = [q[i][0], q[i][1]+1]
        if q and q[0][1] == bridge_length:
            truck = q.popleft()
            total_weight -= truck[0]

        
        if index < len(truck_weights) and total_weight + truck_weights[index]<= weight  and bridge_length >= len(q) :
            q.append([truck_weights[index], 0])
            total_weight += truck_weights[index]
            index += 1
        time += 1

        if not q :
            break
    return time

print(solution(2,10,[7,4,5,6]))
# print(solution(100,100,[10]))
# print(solution(100,100,[10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))


