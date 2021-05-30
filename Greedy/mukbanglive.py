#https://programmers.co.kr/learn/courses/30/lessons/42891

# 무지는 1번 음식부터 먹기 시작하며, 회전판은 번호가 증가하는 순서대로 음식을 무지 앞으로 가져다
# 놓는다.
# 마지막 번호의 음식을 섭취한 후에는 회전판에 의해 다시 1번 음식이 무지 앞으로 온다.
# 무지는 음식 하나를 1초 동안 섭취한 후 남은 음식은 그대로 두고, 다음 음식을 섭취한다.

# 무지가 먹방을 시작한 지 K초 후에 네트워크 장애로 인해 방송이 잠시 중단되었다.
# 무지는 네트워크 정상화 후 다시 방송을 이어갈 때, 몇 번 음식부터 섭취해야 하는지는 알고자 한다.



# food_times : 각 음식을 먹는데 필요한 시간이 음식의 번호 순서대로 들어있는 배열
# k는 방송이 중단된 시간을 의미한다.
# 만약 더 섭취해야 할 음식이 없다면 -1을 반환하면 된다. 

import heapq 

def solution(food_times, k) :
    if sum(food_times) <= k :
        return -1

    q = []
    for i in range(len(food_times)) :
        heapq.heappush(q, (food_times[i], i +1))

    sum_value = 0 #먹기 위해 사용한 시간 
    previous = 0 # 직전에 다 먹은 음식 시간 
    length = len(food_times) # 남은 음식의 개수 

    print(q)

    while sum_value + ((q[0][0] - previous) * length) <= k :
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now
    
    result =  sorted(q, key=lambda x : x[1])
    return result[(k - sum_value) % length][1]


food_times = [3,1,2]
k = 5

print(solution(food_times, k))