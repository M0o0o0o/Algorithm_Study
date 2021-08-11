# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    one = [1,2,3,4,5] * 2001
    two = [2, 1, 2, 3, 2, 4, 2, 5] * 1251
    three = [3,3,1,1,2,2,4,4,5,5] * 1001

    count = [0] * 3
    for i in range(len(answers)) :
        if answers[i] == one[i] :
            count[0] += 1
        if answers[i] == two[i] :
            count[1] += 1
        if answers[i] == three[i] :
            count[2] += 1
    
    high = max(count) 
    result = []

    for i in range(len(count)) : 
        if count[i] == high : 
            result.append(i+1)
    return result


print(solution([[1,3,2,4,2]]))