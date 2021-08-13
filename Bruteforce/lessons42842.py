# https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    total = brown + yellow 
    
    for i in range(total, 2, -1) :
        if total % i == 0 :
            horizontal = total // i 
            vertical = (i-2) * (horizontal-2)

            if vertical == yellow :
                return [i, horizontal]

print(solution(8,1))