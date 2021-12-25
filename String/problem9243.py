# https://www.acmicpc.net/problem/9243

n, prev, afterv = int(input()), list(input()), list(input())

if n % 2 != 0 : 
    for i in range(len(prev)) : 
        if prev[i] == '0' : prev[i] = '1'
        else : prev[i] = '0'
        
if ''.join(prev) == ''.join(after) : print('Deletion succeeded')
else : print('Deletion failed')   