# https://www.acmicpc.net/problem/5026

for _ in range(int(input())) :
    string = list(input().split('+'))
    if string[0] == 'P=NP' :
        print('skipped')
    else :
        print(int(string[0]) + int(string[1]))
    