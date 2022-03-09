# https://programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        num = bin(arr1[i] | arr2[i])[2:]
        num = '0' * (n - len(num)) + num if n - len(num) > 0 else '' + num
        num = [' ' if n == '0' else '#' for n in num]
        answer.append(''.join(num))
    return answer
