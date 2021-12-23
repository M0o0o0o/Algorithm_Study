# https://www.acmicpc.net/problem/9935

string = input()
bomb = input()

stack = []
for i in range(len(string)):
    stack.append(string[i])
    if stack[-1] == bomb[-1] and len(stack) >= len(bomb):
        if ''.join(stack[-len(bomb):]) == bomb:
            for i in range(len(bomb)):
                stack.pop()

if len(stack) > 0:
    print(''.join(stack))
else:
    print('FRULA')
