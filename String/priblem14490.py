# https://www.acmicpc.net/problem/14490

a, b = map(int, input().split(':'))

while True : 
    check = False
    for i in range(2, min(a,b) + 1) : 
        if a % i == 0 and b % i == 0 : 
            check = True
            a, b = a // i, b // i 
    if not check : break
    
print(str(a) + ":" + str(b)) 
        
