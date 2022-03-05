# https://www.acmicpc.net/problem/10178

for _ in range(int(input())):
    candy, child = map(int, input().split())
    print("You get " + str(candy//child) +
          " piece(s) and your dad gets " + str(candy % child) + " piece(s).")
