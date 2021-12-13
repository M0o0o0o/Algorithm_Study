# https://www.acmicpc.net/problem/5598

string = list(input().strip('\n'))
for i in range(len(string)) :
    string[i] = chr(ord(string[i]) - 3 if ord(string[i]) - 3 >= 65 else ord('Z') - (65 - (ord(string[i]) - 2)))
print(''.join(string))
