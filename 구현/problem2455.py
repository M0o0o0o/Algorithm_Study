# https://www.acmicpc.net/problem/2455

answer, people= 0, 0 
for _ in range(4) :
    a, b = map(int,input().split())
    people = people - a + b
    answer = max(answer, people)

print(answer)