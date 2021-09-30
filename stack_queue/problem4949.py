# https://www.acmicpc.net/problem/4949
import sys
input = sys.stdin.readline

while True :
    lst = []
    string = list(input())
    if string[0] == '.'  : break
    check = True
    for s in string : 
        if s in ['(', '['] :
            lst.append(s)
        if s in [')', ']'] :
            if len(lst) > 0 and ((s == ')' and lst[-1] == '(') or (s == ']' and lst[-1] == '['))  :
                lst.pop()
            else :
                check = False
                break
            
    if check and len(lst) ==  0 :
        print('yes')
    else :
        print('no')

        
