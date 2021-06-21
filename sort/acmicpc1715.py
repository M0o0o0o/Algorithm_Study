# # https://www.acmicpc.net/problem/1715
# 이 문제는 N개의 카드 묶음 중에서 가장 작은 수를 갖는 카드 묶음 수 2개를 합하는 과정을
# 반복하면 해결되는 문제인데, 초반에 list에 담아서 sort를 하니 시간 초과가 발생했다.
# 그래서 heapq로 재구현하니 통과했다.

# 항상 우선적으로 주어진 조건과 시간 복잡도를 계산해서 적절한 자료구조로 접근하는 것이 중요하다고 생각한다.
import heapq

n = int(input())
q = []
for _ in range(n):
    num = int(input())
    heapq.heappush(q, num)

result = 0
while len(q) != 1:
    first = heapq.heappop(q)
    second = heapq.heappop(q)

    sumValue = first + second
    heapq.heappush(q, sumValue)

    result += sumValue


print(result)
