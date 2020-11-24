#해당 문제는 '이것이 취업을 위한 코딩 테스트다'의 문제입니다.
'''
'''
n = int(input())
coin = list(map(int,input().split()))
coin.sort()

target = 1
for x in coin :
  if target < x :
    break
  target += x

print(target)