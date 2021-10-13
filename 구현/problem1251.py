# https://www.acmicpc.net/problem/1251

s = input()
answer = []

for i in range(1,len(s)-2) :
    for j in range(i+1, len(s)) :
        a,b,c = s[:i], s[i:j], s[j:]
        answer.append(a[::-1] + b[::-1] + c[::-1])
      
answer.sort()
print(answer[0])
#  0 1 2 3 4 5 6
#  m o b i t e l