# https://www.acmicpc.net/problem/2470
# 산성 용액과 알칼리성 용액의 특성값이 주어졌을 때, 이 중 두 개의 서로 다른 용액을 
# 혼합하여 특성값이 0에 가까운 용액을 만들어내는 두 용액을 찾는 프로그램을 작성하시오.

n = int(input())
lst = list(map(int,input().split()))
lst.sort()

answer = [0,0]
buf = 2000000001
start = 0
end = n-1

while True :     
    if start >= end : 
        break
    sum = lst[start] + lst[end]
    if buf > abs(sum) :
        answer[0], answer[1] = lst[start], lst[end]
        buf = abs(sum)

    if sum > 0 :
        end -= 1
    else :
        start += 1


answer.sort()
print(answer[0], answer[1])