# https://www.acmicpc.net/problem/10992

#    * 4, 0
#   * * 3, 1
#  *   * 1, 3
# *******
n = int(input())
print(' ' * (n-1) + "*")
if(n != 1):
    for i in range(1, n-1):
        print(' ' * (n-1-i) + "*" + ' ' * (2*i-1) + '*')
    print('*' * (2*n-1))
