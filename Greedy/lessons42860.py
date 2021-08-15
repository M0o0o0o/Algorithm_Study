# https://programmers.co.kr/learn/courses/30/lessons/42860

def solution(name):
    name = list(name)
    answer = 0
    index = 0
    while True : 
        answer += min(ord(name[index])-ord('A'), ord('Z')-ord(name[index])+1)
        name[index] = 'A'
        if name.count('A') == len(name) : 
            break
        
        left, right = 1,1
        for r in range(1, len(name)) :
            if name[index + r] != 'A':
                right = r
                break
        for l in range(1, len(name)) :
            if name[index - l] != 'A' :
                left = l
                break
        
        if left < right :
            answer += left
            index -= left
        else :
            answer += right
            index += right

    return answer


print(solution("JAN"))