# https://www.acmicpc.net/problem/12919

def recur(after) :
    global ans 
    if len(before) == len(after) :
        if before == after : ans = True
        return
    
    if after[0] == 'B' : 
        recur(after[1:][::-1])
    if after[-1] == 'A' : 
        recur(after[:len(after)-1])

before  = list(input())
after = list(input())
ans = False
recur(after)

if ans : print('1')
else : print('0')

