# https://www.acmicpc.net/problem/11536

n = int(input())
lst = [input() for _ in range(n)]
sortedLst = sorted(lst)
if ''.join(lst) == ''.join(sortedLst) : 
    print('INCREASING')
elif ''.join(lst) == ''.join(sortedLst[::-1]) :
    print('DECREASING')
else : 
    print('NEITHER')
