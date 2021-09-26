# https://www.acmicpc.net/problem/10886
import math
n = int(input())
num = 0

for _ in range(n) :
    num += int(input())
if num < math.ceil(n / 2) : 
    print('Junhee is not cute!')
else :
    print('Junhee is cute!')