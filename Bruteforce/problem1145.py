# https://www.acmicpc.net/problem/1145

nums = list(map(int, input().split()))
d = 2

while True : 
    count = 0
    for num in nums : 
        if d % num == 0 : count += 1
    if count >= 3 : print(d); break;
    count += 1
    d += 1
    
     
    