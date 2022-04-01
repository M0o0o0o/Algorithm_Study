
import math

n = 3000
array = [True for i in range(n + 1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1


def solution(nums):
    ans = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if array[nums[i] + nums[j] + nums[k]]:
                    ans += 1
    return ans


print(solution([1, 2, 3, 4]))
print(solution([1, 2, 7, 6, 4]))
