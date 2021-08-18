# https://programmers.co.kr/learn/courses/30/lessons/43165
answer = 0
def solution(numbers, target):
    bfs(0, numbers, 0, target) 
    return answer

def bfs(total, numbers, index, target) : 
    global answer
    if index == len(numbers) :
        if total == target :
            answer += 1
        return

    bfs(total + numbers[index], numbers, index+1, target)
    bfs(total - numbers[index], numbers, index+1, target)
    

print(solution([1,1,1,1,1],3))