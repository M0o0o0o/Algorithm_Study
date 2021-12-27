# https://www.acmicpc.net/problem/5789

for _ in range(int(input())) :
    a = input()
    if a[len(a) // 2] == a[len(a) // 2 -1] : print('Do-it') 
    else :print('Do-it-Not')