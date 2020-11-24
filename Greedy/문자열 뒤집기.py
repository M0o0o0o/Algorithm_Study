
다솜이는 0과 1로만 이루어진 문자열 s를 가지고 있습니다. 다솜이는 이 문자열 s에 있는 모든 숫자를 전부 같게 만들려고 합니다. 다솜이가 할 수 있는 행동은 s에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것입니다. 뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미합니다. 문자열 s가 주어졌을 때, 다솜이가 해야 하는 행동의 최소 횟수를 출력하세요.
'''
data = input
zero = 0 
one = 0

if data[0] == '1' :
  zero += 1
else : 
  one += 1

for i in range(len(data) -1) :
  if data[i] != data[i+1]  :
    if data[i+1] == '1' :
      zero += 1
    else :
      one += 1

print(min(zero, one))
