# https://www.acmicpc.net/problem/5586

string = input()
i, iIndex = 0, 0

while True:
    buf = string.find('IOI', iIndex)
    if buf == -1:
        break
    i += 1
    iIndex = buf + 2

print(string.count('JOI'))
print(i)
