# https://www.acmicpc.net/problem/2386

while True : 
    lst = list(input())
    if lst[0] == '#' : break
    print(lst[0], lst.count(lst[0].upper()) + lst.count(lst[0]) - 1)