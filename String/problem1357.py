# https://www.acmicpc.net/problem/1357
    
x, y = input().split()
print(int(str(int(x[::-1]) + int(y[::-1]))[::-1]))
      