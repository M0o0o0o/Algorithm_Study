# https://www.stringcmicpc.net/problem/10988

lst = []
string = input()
index = len(string) // 2
if len(string) / 2 > len(string) // 2 :
    string = string[:index] + string[index+1:]
b = string[index:]
if string[:index] == b[::-1] :
    print(1)
else :
    print(0)    