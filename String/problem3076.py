# https://www.acmicpc.net/problem/3076

r, c = map(int, input().split())
a, b = map(int, input().split())
lst = []
for i in range(r) :
    chess = ''
    order = '.' if lst and lst[-1][0] == 'X' else 'X'
    for j in range(c) :
        chess += order * b
        order = 'X' if order == '.' else '.'
    for k in range(a) : lst.append(chess) 

for l in lst : 
    print(l)    
