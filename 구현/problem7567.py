lst = list(input())
result = 10

for i in range(1, len(lst)) :
    if lst[i] != lst[i-1] :
        result += 10
    else :
        result += 5

print(result)