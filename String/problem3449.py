# https://www.acmicpc.net/problem/3449

for _ in range(int(input())) :
    a, b = input(), input()
    result = 0
    for i in range(len(a)) :
        if a[i] != b[i]: result += 1
    print('Hamming distance is', str(result) + '.')    
    