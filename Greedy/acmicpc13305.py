# https://www.acmicpc.net/problem/13305
# 각 도시에 있는 주유소의 기름 가격과, 각 도시를 연결하는 도로의 길이를 입력으로 받아 제일 왼쪽 도시에서 제일 오른쪽 도시로
# 이동하는 최소의 비용을 계산하는 프로그램을 작성하시오. 

n = int(input())
distance = list(map(int, input().split()))
city = list(map(int, input().split()))

index = 0 
result = 0

while index < n-1 : 
    cost = city[index]
    move = distance[index]

    i = index + 1 
    for j in range(i, n-1) :
        if city[j] > cost : 
            move += distance[j]
            index += 1
        else : 
            break

    result += (cost * move)
    
    index+=1

print(result)
