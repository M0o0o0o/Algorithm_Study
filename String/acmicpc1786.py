# https://www.acmicpc.net/problem/1786
# KMP 알고리즘 

import sys
input = sys.stdin.readline

text = input().replace('\n', "")
pattern = input().replace('\n', "")

ptable = [0 for _ in range(len(pattern))]
j = 0 
for i in range(1, len(pattern)) :
    while j > 0 and pattern[i] != pattern[j] :
        j = ptable[j-1]
    if pattern[i] == pattern[j] :
        j += 1
        ptable[i] = j


j = 0
count = 0
result = []
size = len(pattern)
for i in range(len(text)) :
    while j > 0 and text[i] != pattern[j] :
        j = ptable[j-1]
    if text[i] == pattern[j] :
        if j == size-1 :
            count += 1
            result.append(i-size+2) 
            j = ptable[j]
        else :
            j +=1 
    
print(count)
for i in result :
    print(i)








