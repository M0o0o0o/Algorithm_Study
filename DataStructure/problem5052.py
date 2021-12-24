# https://www.acmicpc.net/problem/

for _ in range(int(input())):
    result = True
    lst, number, n = [set() for _ in range(11)], [], int(input())

    for _ in range(n) :
        number.append(input())
    number.sort(key=len)        
    
    for num in number : 
        lst[len(num)].add(num)
        if not result : break
        for i in range(1, len(num)) :
            if len(lst[i]) > 0 and num[:i] in lst[i] : 
                if num[:i] not in lst[i] : 
                    lst[i].add(num[:i])
                else :
                    result = False
                    break
    if not result : print('NO')
    else : print('YES')
            
            
