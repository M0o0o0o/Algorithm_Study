# https://www.acmicpc.net/problem/1076

lst = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

first = lst.index(input())
second = lst.index(input())
last = lst.index(input())

print(int(str(first) + str(second)) * (10 ** last))