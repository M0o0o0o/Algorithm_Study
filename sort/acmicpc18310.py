n = int(input())

lst = list(map(int, input().split()))
lst = set(lst)
lst = list(lst)
lst.sort()

result = 0
distance = int(1e9)


for i in range(len(lst)):
    total = 0
    for j in range(len(lst)):
        if i == j:
            continue
        total += abs(lst[i] - lst[j])

    if distance > total:
        result = i
        distance = total

print(lst[result])
