# https://www.acmicpc.net/problem/2504

lst = list(input())
stack = []
answer = 0

def func_exit() :
    print(0)
    exit(0)

for i in lst :
    if i == ')' :
        t = 0
        while len(stack) != 0 :
            top = stack.pop()
            if top == '(' :
                if t == 0 :
                    stack.append(2) 
                else :
                    stack.append(2 * t)
                break
            elif top == '[' :
                func_exit()
            else :
                t = t + int(top)
    elif i == ']' :
        t = 0
        while len(stack) != 0 :
            top = stack.pop()
            if top == '[' :
                if t == 0 :
                    stack.append(3) 
                else :
                    stack.append(3 * t)
                break
            elif top == '(' :
                func_exit()
            else :
                t = t + int(top)
    else : stack.append(i)

for i in stack :
    if i == '(' or i == '[' :
        func_exit()
    else :
        answer += i

print(answer)
