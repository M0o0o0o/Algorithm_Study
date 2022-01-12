# https://www.acmicpc.net/problem/4504

n = int(input())
while True:
    num = int(input())
    if num == 0:
        break
    if num % n == 0:
        print(str(num) + " is a multiple of " + str(n) + ".")
    else:
        print(str(num) + " is NOT a multiple of " + str(n) + ".")
