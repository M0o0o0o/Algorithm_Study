n = int(input())

# 왼쪽 오른쪽 위 아래 
r = [0, 0, -1, 1]
c = [-1, 1, 0, 0]
x= 1 
y = 1
plan = int().split()
direcy = ['L', 'R', 'U','D']

for i in plan :
  for j in range (len(plan)) :
    if i == plan[j] :
      nx = x + r[i]
      ny = y + c[i]

  if nx < 1 or ny < 1 or nx > n or ny > n :
    continue

x, y = nx, ny

print(x, y)

