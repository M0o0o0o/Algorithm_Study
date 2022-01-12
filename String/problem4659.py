# https://www.acmicpc.net/problem/4659
vowel = ['a', 'e', 'i', 'o', 'u']
while True:
    s = list(input().strip('\n'))
    if ''.join(s) == 'end':
        break
    check = True
    aeiou = False
    for i in range(len(s)):
        if s[i] in vowel:
            aeiou = True
        if i >= 1 and s[i-1] == s[i] and ''.join(s[i-1: i+1]) not in ['ee', 'oo']:
            check = False
            break
        if i >= 2 and s[i-2] in vowel and s[i-1] in vowel and s[i] in vowel:
            check = False
            break
        if i >= 2 and s[i-2] not in vowel and s[i-1] not in vowel and s[i] not in vowel:
            check = False
            break
    if check and aeiou:
        print('<' + ''.join(s) + '> is acceptable.')
    else:
        print('<' + ''.join(s) + '> is not acceptable.')
