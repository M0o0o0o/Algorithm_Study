# 백준 1427


n = input()
arr = []
for i in range(len(n)) :
    arr.append(int(n[i]))

for i in range(0,len(arr)) : 
    for j in range(i+1, len(arr)) :
        if arr[i] < arr[j] :
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp

for i in arr : 
    print(i, end = '')
