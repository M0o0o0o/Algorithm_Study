total = 0
for i in range(5) :
    score = int(input())
    if score >= 40 :
        total += score
    else :
        total += 40

print(total // 5)