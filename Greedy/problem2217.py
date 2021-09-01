# https://www.acmicpc.net/problem/2217

n = int(input())
rope = []
answer = 0
for i in range(n) :
    rope.append(int(input()))

rope.sort(reverse=True)
for i in range(n) :
    rope[i] = rope[i] * (i+1)

print(max(rope))