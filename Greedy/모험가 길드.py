#해당 문제는 '이것이 취업을 위한 코딩 테스트다'의 문제입니다.
'''
한 마을에 모험가가 N명 있다. 모험가 길드에서는 N명의 모험가를 대상으로 '공포도'를 측정했는데, '공포도'가 높은 모험가는 쉽게 공포를 느껴
위험 상황서 제대로 대처할 능력이 떨어집니다. 모험가 길드장인 동빈이는 모험가 그룹을 안전하게 구성하고자 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있도록 규정했습니다. 동빈이는 최대 몇개의 모험가 그룹을 만들 수 있는지 궁금합니다.
동빈이를 위해 N명의 모험가에 대한 정보다 주어졌을 때, 여행을 떠날 수 있는 그룹 수의 최댓값을 구하는 프로그램을 작성하세요.
'''

n = int(input())
adventurer = list(map(int,input().split()))


#count (정답)
#현재 팀의 인원 
adventurer.sort()
result = 0
person = 0
for i in adventurer :
  person += 1
  if person >= i :
    result += 1
    person = 0

print(result)

''' py 답안 예시 
n = int(input())
data = list(map(int,input().split()))
result = 0 
count = 0

for i in data :
  count += 1
  if count >= i :
    result += 1
    count = 0 

print(result)
'''