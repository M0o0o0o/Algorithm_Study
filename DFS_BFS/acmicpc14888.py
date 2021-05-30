#https://www.acmicpc.net/problem/14888



def solution(number, index, operator) :
    if index == n : 
        global resultMin
        global resultMax 
        resultMax = max(resultMax, number)
        resultMin = min(resultMin, number)
        return
    
    for i in range(4) :
        if operator[i] > 0 :
            if i == 0 :
                operator[i] -= 1
                solution(number+numbers[index], index+1, operator) 
                operator[i] += 1
            elif i == 1 :
                operator[i] -= 1
                solution(number-numbers[index], index+1, operator) 
                operator[i] += 1
            elif i == 2 :
                operator[i] -= 1
                solution(number*numbers[index], index+1, operator) 
                operator[i] += 1
            else :
                operator[i] -= 1
                solution(int(number / numbers[index]), index+1, operator) 
                operator[i] += 1                    
    return 


n = int(input())

numbers = []
numbers = list(map(int,input().split()))

op = []
# 덧셈, 뺼셈, 곱셈, 나눗셈
op = list(map(int,input().split()))

resultMin = int(1e9)
resultMax= int(1e9) * -1


solution(numbers[0], 1, op)

print(resultMax)
print(resultMin)
