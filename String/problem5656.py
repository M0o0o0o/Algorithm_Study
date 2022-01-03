# https://www.acmicpc.net/problem/5656

i = 1
while True : 
    lst = list(input().split(' '))
    check = False
    if lst[1] == 'E' : break
    if lst[1] == '>' and int(lst[0]) > int(lst[2]) : check = True
    elif lst[1] == '>=' and int(lst[0]) >= int(lst[2]) : check = True
    elif lst[1] == '<' and int(lst[0]) < int(lst[2]) : check = True
    elif lst[1] == '<=' and int(lst[0]) <= int(lst[2]) : check = True
    elif lst[1] == '==' and int(lst[0]) == int(lst[2]) : check = True
    elif lst[1] == '!=' and int(lst[0]) != int(lst[2]) : check = True
    if check : 
        print('Case ' + str(i) + ": true",)
    else :
        print('Case ' + str(i) + ": false",)
    i += 1    

        