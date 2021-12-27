# https://www.acmicpc.net/problem/9996

n = int(input())
pattern = input().split('*')

for i in range(n) :
    string = input()
    if string[:len(pattern[0])] == pattern[0] and string[-len(pattern[1]):] == pattern[1] and len("".join(pattern)) <= len(string) :
        print('DA')
    else : 
        print('NE')     