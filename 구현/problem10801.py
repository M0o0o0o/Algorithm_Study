
lst = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
a, b = 0, 0
for i in range(10):
    if lst[i] > lst2[i]:
        a += 1
    elif lst[i] < lst2[i]:
        b += 1

if a > b:
    print('A')
elif a < b:
    print('B')
else:
    print('D')
