a, b = map(int,input().split())
answer = int(1e9) 

def solution(a, b, count) :
    global answer
    if a > b :
        return
    if a == b :
        answer = min(answer, count)
    solution(a * 2, b, count + 1) 
    solution(int(str(a) + "1"), b, count + 1) 

    return 

solution(a,b,0)
if answer == int(1e9) :
    print(-1) 
else : 
    print(answer + 1)
