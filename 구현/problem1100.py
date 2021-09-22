# https://www.acmicpc.net/problem/1100
lst = []
for _ in range(8) :
    lst.append(list(input()))     
answer = 0
for i in range(8) :
    white = True 
    if i % 2 == 1 :
        white = False 
    for c in lst[i] :
        if white and c == 'F' :
            answer += 1
        white = not white
        

print(answer)
