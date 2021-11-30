# https://www.acmicpc.net/problem/23742
import sys; input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
lst.sort(reverse=True)
plus, one, minus1, minus2, count = 0, 0, 0, 0, 0

def check(l) : 
    return (plus * (count + 1)) + (one * (count + 1)) + ((minus1 + l) * (count +1)) + minus2
def calculator() :
    return (plus * (count)) + (one * (count)) + ((minus1) * (count)) + minus2

for l in lst : 
    if l == 1 : 
        count += 1
        one += 1
    elif l == 0 :
        count += 1
    elif l > 1 : 
        count += 1
        plus += l 
    else : 
        if check(l) > calculator() + l :
            minus1 += l
            count += 1
        else : 
            minus2 += l
            
print(calculator())
