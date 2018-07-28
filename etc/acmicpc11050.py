from itertools import combinations

n, k = map(int,input().split())

lst = [i for i in range(1, n+1)]
print(len(list(combinations(lst, k))))
