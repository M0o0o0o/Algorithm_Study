# https://www.acmicpc.net/problem/7600

while True : 
    S = input()
    dic = dict()
    if S == '#' : break
    for s in S : 
        if s.isalpha() :
            dic[s.lower()] = 1
    print(len(dic)) 
            