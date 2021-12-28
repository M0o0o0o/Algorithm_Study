# https://www.acmicpc.net/problem/10833

ans = 0
for _ in range(int(input())):
    student, apple = map(int, input().split())
    ans += apple % student
print(ans)
