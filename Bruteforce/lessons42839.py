# https://programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations

import math


def solution(numbers):
    count = [False] * 10000000
    n = 9999999
    prime = [True for i in range(10000000)] 
    for i in range(2, int(math.sqrt(10000000)) + 1): 
        if prime[i] == True: 

            j = 2 
            while i * j <= n:
                prime[i * j] = False
                j += 1


    answer = 0
    numbers = list(numbers)
    for i in range(1,len(numbers) + 1) :
        permu = list(permutations(numbers,i))
        for j in range(len(permu)) :
            buf = list(permu[j])
            buf = int(''.join(buf))
            if buf == 0 or buf == 1 :
                continue
            if count[buf] == False :
                if prime[buf] :
                    answer += 1
                    count[buf] = True
             
    return answer

print(solution("011"))


