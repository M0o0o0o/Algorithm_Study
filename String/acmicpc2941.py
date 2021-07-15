# https://www.acmicpc.net/problem/2941

lst = ['c=', 'c-','dz=','d-','lj','nj','s=','z=']

str = input()
index = 0 
result = 0 

def check(buf) :
    for s in lst : 
        if buf == s :
            return True

while index < len(str) :
    if index + 3 <= len(str) :
        buf = str[index : index + 3] 
        if buf == 'dz=' :
            index += 3
            result += 1
            continue

    if index + 2 <= len(str) :
        buf = str[index : index + 2]
        if check(buf) :
            index += 2 
            result += 1
            continue
    index += 1
    result += 1


print(result)
