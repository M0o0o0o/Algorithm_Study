# https://www.acmicpc.net/problem/3028

string = input() 
ans = 1 

for s in string : 
    if s == 'A' : 
        if ans == 1 : ans = 2
        elif ans == 2 : ans = 1
    elif s == 'B' : 
        if ans == 2 : ans = 3 
        elif ans == 3 : ans = 2
    else : 
        if ans == 1 : ans = 3
        elif ans == 3 : ans = 1
    
print(ans)
    
