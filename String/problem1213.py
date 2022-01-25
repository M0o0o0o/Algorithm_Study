# https://www.acmicpc.net/problem/1213
S = input()
alpha = [0] * 26
left, right, middle = '', '', ''
for s in S:
    alpha[ord(s)-65] += 1
for i in range(26):
    if alpha[i] >= 2:
        left += chr(i + 65) * (alpha[i] // 2)
        right += chr(i + 65) * (alpha[i] // 2)
        alpha[i] %= 2
    if alpha[i] == 1:
        middle += chr(i + 65)
        alpha[i] -= 1

ans = left + middle + right[::-1]
if ans == ans[::-1]:
    print(ans)
else:
    print("I'm Sorry Hansoo")
