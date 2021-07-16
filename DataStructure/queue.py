from collections import deque
#주로 코딩테스트에서는 deque를 활용해 큐를 구현한다.
queue = deque()

queue.append(5);
queue.append(2);
queue.append(3);
queue.append(7);
queue.popleft()
print(queue)
print(type(queue))
queue.append(9)
print(queue)