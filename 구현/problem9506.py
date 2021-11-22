# https://www.acmicpc.net/problem/9506

while True :
    n = int(input())
    if n == -1 : break
    lst = [] 
    for i in range(1, n) :
        if n % i == 0 :
            lst.append(i)
            
    if sum(lst) != n : 
        print(n, 'is NOT perfect.') 
        continue
    print(n, '= ', end = '')
    for i in range(len(lst)) :
        if i+1 == len(lst) : print(lst[i])
        else : print(lst[i], end = ' + ')
    

        