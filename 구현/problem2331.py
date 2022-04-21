# https://www.acmicpc.net/problem/2331


a, p = map(int, input().split())
lst = [a]
dic = {a: 0}

while True:
    num = 0
    for s in list(str(lst[-1])):
        num += int(s) ** p
    if num not in dic:
        lst.append(num)
        dic[num] = len(lst) - 1
        continue
    print(len(lst[:dic[num]]))
    break
