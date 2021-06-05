#해당 문제는 '이것이 취업을 위한 코딩 테스트다'의 문제입니다.
'''
N명의 학생 정보다 있다. 학생 정보는 이름과 학생의 성적으로 구분된다.각
학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 
학생의 이름을 출력하는 프로그램을 작성하시오.
'''



n = int(input())
student = []

for i in range(n) :
  data = input().split()
  student.append((data[0], int(data[1])))

student = sorted(student, key = lambda students : students[1])

for name in student : 
  print(name[0], end = ' ')
