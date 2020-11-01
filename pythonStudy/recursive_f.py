a = 10

def recur() :
  global a
  a -= 1
  if a >= 1 :
    print(a)
    recur()
  