# https://www.acmicpc.net/problem/2592

average = 0 
frequency = 0
lst = []
for _ in range(10) :
    lst.append(int(input()))
    average += lst[-1]

count = 0
for num in lst : 
    if lst.count(num) > count :
        count = lst.count(num)
        frequency = num

print(average // 10)
print(frequency)