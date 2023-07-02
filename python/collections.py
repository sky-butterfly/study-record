from collections import deque, Counter

# queue

queue = deque([1, 2, 3])

# queue 삽입
queue.appendleft(0)
queue.append(4)

print(queue)

# queue 제거
queue.popleft()
queue.pop()

print(queue)

# counter

counter = Counter([1, 1, 2, 2, 3, 3, 3])

print(counter[1])
print(dict(counter))