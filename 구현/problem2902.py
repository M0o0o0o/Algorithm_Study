# https://www.acmicpc.net/problem/2902

names = input()
names = names.split('-')
for name in names : 
    print(name[0], end = '')