# https://www.acmicpc.net/problem/2864

a, b = input().split()
a, b = list(a), list(b)
a = ['5' if a[i] == '6' else a[i] for i in range(len(a))]    
b = ['5' if b[i] == '6' else b[i] for i in range(len(b))]    
print(int(''.join(a)) + int(''.join(b)), end = ' ')
a = ['6' if a[i] == '5' else a[i] for i in range(len(a))]    
b = ['6' if b[i] == '5' else b[i] for i in range(len(b))]    
print(int(''.join(a)) + int(''.join(b)))
