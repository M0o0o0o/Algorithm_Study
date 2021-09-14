n, m = map(int,input().split())

j = int(input())
left, right = 1, m
answer = 0
for i in range(j) :
    apple = int(input())

    if apple < left :
        answer += (left - apple)
        right -= (left - apple)
        left = apple 
    elif apple > right : 
        answer += (apple - right)
        left += (apple -right)
        right = apple
print(answer)