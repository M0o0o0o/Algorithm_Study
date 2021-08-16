# https://programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    stack = [number[0]]
    for n in number[1:] :
        while len(stack) > 0 and stack[-1] < n and k > 0 :
            k -= 1
            stack.pop()
        stack.append(n)
    if k != 0 :
        stack = stack[:-k]
    return ''.join(stack)

print(solution("4177252841",4))