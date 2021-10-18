# https://www.acmicpc.net/problem/23080
n = int(input())
secret = input()
answer = secret[0]

index = n
while True :
    if index >= len(secret) : break
    answer += secret[index] 
    index += n

print(answer)


