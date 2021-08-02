def solution(participant, completion): 
    dic = dict()
    value = 0

    for p in participant :
        dic[hash(p)] = p;
        value += hash(p)

    for c in completion : 
        value -= hash(c)

    return dic[value]


