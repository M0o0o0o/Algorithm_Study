
lst, lst2 = [], []

for _ in range(10) :
    lst.append(int(input()))
    
for _ in range(10) :
    lst2.append(int(input()))

lst.sort(reverse=True)
lst2.sort(reverse=True)

print(sum(lst[:3]), sum(lst2[:3]))