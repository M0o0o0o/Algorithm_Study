# https://www.acmicpc.net/problem/4458

for _ in range(int(input())) : 
    string = list(input())
    string[0] = string[0].upper()
    print(''.join(string))
