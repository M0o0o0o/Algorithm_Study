'''
삽입 정렬은 특정한 데이터를 적절한 위치에 '삽입'한다는 의미에서 삽입 정렬이라고 부른다. 더불어 삽입 정렬은 특정한 데이터가 적절한 위치에 들어가기 이전에, 그 앞까지의 데이터는 이미 정렬되어 있다고 가정한다

'''

#구현
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)) :
  for j in range(i, 0, -1) :
    if(array[j] < array[j-1]) :
      array[j], array[j-1] = array[j-1], array[j]
    else :
      break
print(array)