# https://www.acmicpc.net/problem/3059

for _ in range(int(input())) :
    alpha = [0] * 26 
    for a in list(input().strip('\n')) :
        alpha[ord(a)-65] += 1
    answer = 0
    for i in range(26) :
        if alpha[i] == 0 : answer += i + 65
    print(answer) 
    
    
    
