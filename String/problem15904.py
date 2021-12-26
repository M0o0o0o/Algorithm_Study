# https://www.acmicpc.net/problem/15904

string = input()
ans = True

for c in ['U', 'C', 'P', 'C']:
    if c in string:
        string = string[string.find(c)+1:]
        continue
    ans = False
    break

if ans:
    print('I love UCPC')
else:
    print('I hate UCPC')
