# https://www.acmicpc.net/problem/1193

x = int(input())
up = [-1, 1]
down = [1, -1]
row = col = 1
cycle = True

for i in range(2, x+1) :
    if cycle : 
        if row != 1 :
            row += up[0]
            col += up[1] 
        else :
            col += 1
            cycle = False
    else :
        if col !=  1 :
            row += down[0]
            col += down[1] 
        else : 
            row += 1
            cycle = True

print(str(row) + '/' + str(col))

