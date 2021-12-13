# https://www.acmicpc.net/problem/2744

string = list(input().strip('\n'))

for s in string : 
    if s.isupper() : print(s.lower(), end = '')
    else : print(s.upper(), end = '')
    