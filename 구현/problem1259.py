# https://www.acmicpc.net/problem/1259

lst = []
while True :
    string = input()
    if string == '0' : break
    lst.append(string)

for i in range(len(lst)) :
    a = lst[i]
    index = len(a) // 2
    if len(a) / 2 > len(a) // 2 :
        a = a[:index] + a[index+1:]
    b = a[index:]
    if a[:index] == b[::-1] :
        print('yes')
    else :
        print('no')    
    

         

