# https://www.acmicpc.net/problem/2153

num = 0
for i in list(input().strip('\n')) :
    if ord(i) >= 97 : num += ord(i) - 96
    else : num += ord(i) - 38
        
prime = True
for i in range(2, num) : 
    if num % i == 0 : 
        prime = False
        break
if prime : print('It is a prime word.') 
else : print('It is not a prime word.')