score = input()

num1 = 0;
num2 = 0;

for i in range(int(len(score)/2)) :
        num1 = num1 + int(score[i])

for j in range(int(len(score)/2), len(score)) :
      num2 = num2 + int(score[j]);

if num1 == num2 : print("LUCKY")
else : print("READY")