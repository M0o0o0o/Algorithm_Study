# https://www.acmicpc.net/problem/1450
# 세준이는 N개의 물건을 가지고 있고, 최대 C만큼의 무게를 넣을 수 있는 가방을 하나 가지고 있다.
# N개의 물건을 가방에 넣는 방법의 수를 구한느 프로그램을 작성하시오

# 아무것도 넣지 않는 것도 포함한다. 
# c의 범위가 최대10^9-1 dp로는 풀 수 없다. 


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

print(asum)
print(bsum)
result = 0

for i in asum :
    if c - i < 0 :
        continue
    result += binary(c-i, 0, len(bsum))

print(result)


# import sys 
# n, c = map(int, input().split())
# weight = list(map(int, input().split()))

# aw = weight[:n//2]
# bw = weight[n//2:]

# asum = []
# bsum = []

# def bruteforce(warr, sumarr, l, w) :
#     if l >= len(warr) :
#         sumarr.append(w)
#         return

#     bruteforce(warr, sumarr, l+1, w)
#     bruteforce(warr, sumarr, l+1, w + warr[l])


# def binarysearch(arr, target, start, end) :
#     while start < end :
#         mid = (start + end) // 2
#         if arr[mid] <= target :
#             start = mid + 1
#         else :
#             end = mid
#     return end

# bruteforce(aw, asum, 0, 0)
# bruteforce(bw, bsum, 0, 0)  
# bsum.sort()

# cnt = 0
# for i in asum :
#     if c- i < 0 :
#         continue
#     cnt  += binarysearch(bsum, c-i, 0, len(bsum))
# print(cnt)
    