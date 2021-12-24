# https://www.acmicpc.net/problem/1517


# def mergeSort(lst) :
#     global ans
#     n = len(lst)
    
#     if n <= 1 : return
    
#     mid = n // 2 
#     lefts = lst[:mid]
#     rights = lst[mid:] 
    
#     mergeSort(lefts)
#     mergeSort(rights)
    
#     left, right, now = 0, 0, 0
    
#     while left < len(lefts) and right < len(rights) : 
#         if lefts[left] < rights[right] :
#             lst[now] = lefts[left]
#             left += 1
#             now += 1
#             ans += 1
#         else :
#             lst[now] = rights[right]
#             right += 1
#             now += 1
#             ans += 1
    
#     while left < len(lefts) :
#         lst[now] = lefts[left]
#         left += 1
#         now += 1
#     while right < len(rights) :
#         lst[now] = rights[right]
#         right += 1
#         now += 1
        
        
# N = int(input())
# lst = list(map(int, input().split()))
# ans = 0

# mergeSort(lst) 
# print(ans)



def bubble_sort(arr):
    global ans
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                ans += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
arr = [5,4,3,2,1]
ans = 0

bubble_sort(arr)
print(ans)