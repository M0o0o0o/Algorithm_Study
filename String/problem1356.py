# https://www.acmicpc.net/problem/1356

def calculator(buf) :
    result = buf[0]
    for i in range(1, len(buf)) :
        result *= buf[i]
    return result

num = list(map(int, input()))
check = 'NO'

if len(num) > 1 :
    for i in range(len(num)-1) :
        if calculator(num[:i+1]) == calculator(num[i+1:]) :
            check = 'YES'
            break
        
print(check)

