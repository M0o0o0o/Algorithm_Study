# https://www.acmicpc.net/problem/1789

s = int(input())
num = 1
total = 0
answer = 0 

while total < s :
    total += num 
    num += 1
    answer += 1

if total == s : 
    print(answer)
else :
    print(answer - 1)