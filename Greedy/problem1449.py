# https://www.acmicpc.net/problem/1449

n, tape = map(int,input().split())
place = list(map(int,input().split()))
place.sort()
answer = 0 
tape_location = -2
for i in range(n) :
    if place[i] > tape_location :
        tape_location = place[i] + tape -1 
        answer += 1

print(answer)