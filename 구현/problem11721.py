# https://www.acmicpc.net/problem/11721

string =  ' ' + input()

for i in range(1 ,len(string)) :
    if i % 10 == 0  :
        print(string[i])
    else :
        print(string[i], end = '')