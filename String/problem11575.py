# https://www.acmicpc.net/problem/11575

for _ in range(int(input())) : 
    a, b = map(int, input().split())
    string = list(input())
    for i in range(len(string)) :
        string[i] = chr((a * (ord(string[i]) - 65) + b) % 26 + 65)
    print(''.join(string))
    
    