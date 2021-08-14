# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    lst = [1] * n
    count = 0
    for i in lost :
        lst[i-1] -= 1
    for i in reserve : 
        lst[i-1] += 1
    for i in range(len(lst)) :
        if lst[i] == 2 and i-1 >= 0 and lst[i-1] == 0 :
            lst[i-1] = 1
            lst[i] = 1
        if lst[i] == 2 and i+1 < n and lst[i+1] == 0 :
            lst[i+1] = 1
            lst[i] = 1
            
    for i in lst :
        if i >= 1 : 
            count += 1

    return count

print(solution(3,[3],[1]))