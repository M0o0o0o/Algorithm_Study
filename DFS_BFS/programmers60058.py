# https://programmers.co.kr/learn/courses/30/lessons/60058
# '(' 와 ')' 로만 이루어진 문자열 w가 "균형잡힌 괄호 문자열" 이라면 다음과 같은 과정을 통해 "올바른 괄호 문자열"로 변환할 수 있습니다.

# 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
# 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
# 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
#   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
# 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
#   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
#   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
#   4-3. ')'를 다시 붙입니다. 
#   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
#   4-5. 생성된 문자열을 반환합니다.


def rightBracket(p) :
    stack = []
    
    for i in p :
        if i == '(' :
            stack.append('(')
        else :
            if len(stack) != 0 :
                stack.pop()
            else :
                return False
    
    return True

def balanced(p) :
    count = 0
    for i in range(len(p)) :
        if p[i] == '(' :
            count += 1
        else :
            count -= 1
        
        if count == 0 :
            return i 



def solution(p):
    answer = '';
    if p == '' :
        return answer 

    index = balanced(p)
    u = p[:index+1]
    v = p[index+1:]

    if rightBracket(u) :
        answer = u + solution(v) 
    else :
        answer = '('
        answer += solution(v)
        answer += ')'

        u = list(u[1:-1])
        for i in range(len(u)) :
            if u[i] == ')' :
                u[i] = '('
            else :
                u[i] = ')'
        
        answer += "".join(u)

    return answer


print(solution("()))((()"))