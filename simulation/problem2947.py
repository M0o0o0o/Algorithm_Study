# https://www.acmicpc.net/problem/2947

lst = list(map(int, input().split()))
flag = False
while not flag:
    for i in range(1, len(lst)):
        if lst[i-1] > lst[i]:
            lst[i-1], lst[i] = lst[i], lst[i-1]
            print(*lst)
        if ''.join(list(map(str, lst))) == "12345":
            flag = True
            break
