# https://www.acmicpc.net/problem/14405

s = input()
if s.count('pi') * 2 + s.count('ka') * 2 + s.count('chu') * 3 == len(s):
    print('YES')
else:
    print('NO')
