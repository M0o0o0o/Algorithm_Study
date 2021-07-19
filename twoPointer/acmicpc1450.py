# https://www.acmicpc.net/problem/1450
# 세준이는 N개의 물건을 가지고 있고, 최대 C만큼의 무게를 넣을 수 있는 가방을 하나 가지고 있다.
# N개의 물건을 가방에 넣는 방법의 수를 구한느 프로그램을 작성하시오


n, c = map(int, input().split())
lst = list(map(int,input().split()))

aw = lst[:n//2]
bw = lst[n//2:]

asum = []
bsum = []


def recur(arr, wsum, l ,w) :
    if l >= len(arr) :
        wsum.append(w)
        return
    
    recur(arr, wsum, l+1, w)
    recur(arr, wsum, l+1, w + arr[l])


def binary(target, start, end) :
    while start < end :
        mid = (start+end) // 2
        if bsum[mid] <= target :
            start = mid + 1
        else :
            end = mid
    return end 


recur(aw, asum, 0, 0)
recur(bw, bsum, 0, 0)

bsum.sort()
result = 0

for i in asum :
    if c - i < 0 :
        continue
    result += binary(c-i, 0, len(bsum))

print(result)
