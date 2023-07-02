import heapq

h = []

# 삽입
for i in range(5):
    heapq.heappush(h, i)

print(h)

# 꺼내기
for i in range(5):
    print(heapq.heappop(h))

print(h)

# 삽입 후 다시 꺼내면 정렬이 됨


