# https://www.acmicpc.net/problem/17450
snack = ['S', 'N', 'U']
lst = []
for i in range(3):
    price, weight = map(int, input().split())
    price = price * 10 if price * 10 < 5000 else (price * 10) - 500
    lst.append((weight / price, snack[i]))

lst.sort(reverse=True)
print(lst[0][1])
