# https://www.acmicpc.net/problem/1371
import sys

s = sys.stdin.read()
alpha = [0]*26
for c in s:
    if c.islower():
        alpha[ord(c)-97] += 1
for i in range(26):
    if alpha[i] == max(alpha):
        print(chr(97+i), end='')
