# 도3 개2 걸1 윷0 모4

lst = ['D', 'C', 'B', 'A', 'E']

for _ in range(3) :
    play = list(map(int,input().split()))
    print(lst[sum(play)])