# https://www.acmicpc.net/problem/10991

n = int(input())

for i in range(n-1, -1, -1) :
    star = n - i
    prev = False 
    for j in range(i) : print(' ', end ='')
    while star > 0 :
        if not prev :
            print('*', end='')
            star -= 1
        else : print(' ', end ='')
        prev = not prev
        
    print()
        


