#해당 문제는 '이것이 취업을 위한 코딩 테스트다'의 문제입니다.
'''
A, B 두 사람이 볼링을 치고 있습니다. 두 사람은 서로 무게가 다른 볼링공을 고르려고 합니다. 볼링공은 총 N개가 있으며 각 볼링공마다 무게가 적혀 있고,
공의 번호는 1번부터 순서대로 부여됩니다. 또한 같은 무게의 공이 여러 개 있을 수 있지만, 서로 다른 공으로 간주합니다. 볼링공의 무게는 1부터 M까지의 자연수 형태로 존재합니다.
'''

#첫번째 답
# n, m = map(int,input().split())
# ball = list(map(int, input().split()))

# result = 0

# for i in range(0, len(ball)) :
#   for j in range(i+1, len(ball)) :
#     if ball[i] != ball[j] : 
#       result += 1

# print(result)


# 계수정렬을 이용한 두번째 답 

# n, m = map(int,input().split())
# data = list(map(int, input().split()))
# ball = [0] * 11
# result = 0

# for i in data :
#   ball[i] += 1

# for i in range(1, len(ball)) :
#   for j in range(i+1, len(ball)) :
#     if i != 0 and j != 0 :
#       result += ball[i] * ball[j]

# print(result)


#답안 예시
n, m = map(int,input().split())
data = list(map(int,input().split()))

array = [0] * 11

for x in data :
  array[x] += 1

result = 0
for i in range(1, m+1) :
  n -= array[i]
  result += array[i]

print(array)