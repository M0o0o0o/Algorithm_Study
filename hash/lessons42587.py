def solution(clothes):
    dic = dict()
    for cloth, sort in clothes : 
        if sort in dic :
            dic[sort] = dic[sort] + 1
        else :
            dic[sort] = 1

    result = 1 

    for k in dic :
        result *= (dic[k] + 1)
    
    return result -1

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
