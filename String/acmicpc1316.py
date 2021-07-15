# https://www.acmicpc.net/problem/1316

n = int(input())
lst = []

for _ in range(n) :
    lst.append(input())

result = n

for i in range(n) :
    str = lst[i]
    alpha = [0] * 26
    alpha[ord(str[0])-97] = 1
    for i in range(1, len(str))  :
        index = ord(str[i])-97
        if alpha[index] == 0 :
            alpha[index] += 1
        elif alpha[index] == 1 and str[i] == str[i-1] :
            continue
        else :
            result -= 1
            break

print(result)

