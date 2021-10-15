# https://www.acmicpc.net/problem/11656

string = input()
answer = []

for i in range(len(string)) :
    buf = list(string[i:])
    answer.append(''.join(buf))

answer.sort()
for i in answer :
    print(i)
