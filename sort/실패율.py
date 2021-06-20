# https://programmers.co.kr/learn/courses/30/lessons/42889?language=python3

# 전체 스테이지 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때
# 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨 있는 배열을 return 하도록 solution 함수를 완성

# 실패율 : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어의 수 
# 만약 실패율이 같은 스테이지가 있디만 작은 번호의 스테이지가 먼저 오도록 하면 된다.
# 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0으로 정의한다. 


# graph = [[] for _ in range(comCount+1)]
def solution(N, stages):
    
    answer = []
    length = len(stages)
    print('length : ', length)

    for i in range(1, N+1) :
        count = stages.count(i)

        if length == 0 :
            fail = 0
        else :
            fail = count / length

        answer.append((i, fail))

        length -= count 

    answer = sorted(answer, key=lambda t : t[1], reverse=True)

    answer = [i[0] for i in answer]
    return answer 


solution(5, [2,1,2,6,2,4,3,3])