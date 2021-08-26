# https://www.acmicpc.net/problem/1439

card = list(input())
answer = len(card) + 1000

def calculator(card, target, num, reverse) :
    if reverse :
        for i in range(len(card)) :
            if card[i] == "1" :
                card[i] = "0"
            else :
                card[i] = "1"
    count = 0 
    for i in range(len(card)) :
        if card[i] == target :
            if i > 0 and card[i-1] == num :
                count += 1 
            elif i > 0 and card[i-1] == target :
                continue 
            else :
                count += 1

    if reverse : 
        return count + 1
    return count 

answer = min(answer, calculator(card, "1", "0", False))
answer = min(answer, calculator(card, "0", "1", False))
answer = min(answer, calculator(card, "0", "1", True))
answer = min(answer, calculator(card, "0", "1", True))
print(answer)
            

