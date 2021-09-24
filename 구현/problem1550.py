# https://www.acmicpc.net/problem/1550

numbers = list(input())
numbers.reverse()
answer = 0 

for i in range(len(numbers)) :
    num = numbers[i]
    if ord(num) >= 65 :
        num = ord(num) - 55 
    else :
        num = ord(num) - 48
    answer += num * (16 ** i)

print(answer)
    