# https://www.acmicpc.net/problem/2703

for _ in range(int(input())) :
    string, ecrypt = list(input()), list(input())
    [print(ecrypt[ord(s) - 65], end = '') if 'A' <= s <= 'Z' else print(s, end = '')  for s in string ]
    print()