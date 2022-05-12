# https://www.acmicpc.net/problem/9366

# “equilateral”, “isosceles”, “scalene”
# Case #1: isosceles
# Case #2: invalid!

for i in range(int(input())):
    lst = list(map(int, input().split())
    print('Case #' + str(i+1) + ": ", end='')
    if lst.count(lst[0]) == 3:
        print('equilateral')
    elif lst.count(lst[0]) == 2 or lst.count(lst[0]) == 2:
        print('isosceles')
    else:
        print('scalene')
