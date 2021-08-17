# https://programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    people.sort()
    start, end = 0, len(people)-1 
    answer = 0
    while start <= end :
        answer += 1
        if people[start] + people[end] <= limit :
            start += 1
        end -= 1
    return answer              

print(solution([70, 50, 80],100))
