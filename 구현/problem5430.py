# https://www.acmicpc.net/problem/5430

from collections import deque

def R_method(number, index) :
    if index == 0 :
        return len(number) -1 
    return 0

def D_method(number, index) :
    if index == 0 :
        number.popleft()
        return 0 
    else :
        number.pop()
        return len(number) - 1

for _ in range(int(input())) :
    method = list(input())
    number = int(input())
    string = input()
    number = deque([])
    index = 0
    
    buf = ''
    for i in range(len(string)) :
        if 48 <= ord(string[i]) <= 57 :
            buf += string[i]
        else :
            if len(buf) > 0 :
                number.append(int(buf))
                buf =''

    for m in method : 
        if m == 'R' : 
            index = R_method(number, index) 
        else :
            if len(number) == 0 :
                number = 'error'
                break
            index = D_method(number, index)

    if number != 'error' :
        number = list(number)
        if index == len(number) -1 :
            number.reverse()
        print('[', end ='')
        for i in range(len(number)) :
            if i != 0 :
                print(',',end ='')
            print(number[i], end='')
        print(']')
    else :
        print('error')

            

