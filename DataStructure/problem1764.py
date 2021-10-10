# https://www.acmicpc.net/problem/1764

n, m = map(int,input().split())
notHear, notSee, answer = [], [], []

for _ in range(n) :
    notHear.append(input())
for _ in range(m) :
    notSee.append(input())

notSee = set(notSee)

for h in notHear : 
    if h in notSee :
        answer.append(h)

answer.sort()

print(len(answer))
for a in answer :
    print(a)