list = [1, 2, 3, 4, 5]


# 인덱싱
first = list[0] 
print(first) # 1
last = list[-1]
print(last) # 5

# 슬라이싱
firstSecond = list[0:2]
print(firstSecond) # [1,2]
third = list[:3]
print(third) # [1,2,3]

# 길이
size = len(list)
print(size) # 5

# 삭제
del list[2]
print(list) # [1,2,4,5]

# 요소추가
a = list.append(6)
print(a) # None
print(list) # [1,2,4,5,6]

# 정렬
list.sort()

# 뒤집기
list.reverse()
print(list) # [6,5,4,2,1]

# 위치반환 (요소 입력)
i = list.index(6)
print(i) # 0

# 요소 삽입 (인덱스, 요소)
list.insert(0, 7)
print(list) # [7,6,5,4,2,1]

# 요소 제거 (요소입력)
list.remove(4)
print(list) # [7,6,5,2,1]

# 요소 끄집어내기 (인덱스입력)
p = list.pop()
print(p) # 1
p = list.pop(0)
print(p) # 7

# 포함된 요소 개수
c = list.count(2)
print(c) # 1

# 확장
list.extend([8,9])
print(list) # [6,5,2,8,9]