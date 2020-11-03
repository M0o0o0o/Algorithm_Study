#해당 문제는 '이것이 취업을 위한 코딩 테스트다'의 문제입니다.
n = int(input())

count = 0 

for i in range(n) :
  for j in range(60) :
    for k in range(60) :
      if '3' in str(i) + str(j) + str(k) :
        count += 1

print(count) 