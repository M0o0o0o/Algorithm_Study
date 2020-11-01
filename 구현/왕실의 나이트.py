#행은 숫자, 열은 a~h
data = input();
row = data[1]-1
col = (int(ord(data[0])) - int(ord('a')))  + 1

move = [(-2, 1), (-2, -1), (2, 1), (-2,-1), (1,-2), (1,2), (1,2),(-1,2)]
result = 0
for index in move : 
  next_row = row + index[0]
  next_col = col + index[1]

  if next_row < 1 or next_col < 1 or next_row > 8 or next_col > 8 :
    continue
  
  result += 1
