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
list = [2, 1, 3]
list.sort()
print(list) # [1, 2, 3]

# 내림차순 정렬
list = [1, 2, 3]
list.sort(reverse=True)
print(list) # [3, 2, 1]

# list 존체는 변형하지 않고 정렬값 반환
list = [2, 1, 3]
print(sorted(list)) # [1, 2, 3]
print(list) # [2, 1, 3]

# 뒤집기
list.reverse()
print(list) # [6,5,4,2,1]

# 위치반환 (요소 입력)
list = [6, 2, 1]
i = list.index(6)
print(i) # 0

list = [1, 1, 1]
print('index : ', list.index(1)) # 0

# 요소 삽입 (인덱스, 요소)
list.insert(0, 7)
print(list) # [7,6,5,4,2,1]

# 요소 제거 (요소입력)
list = [7,6,5,2,1,4]
list.remove(4)
print(list) # [7,6,5,2,1]

# 요소 끄집어내기 (인덱스입력)
list = [7,1]
p = list.pop()
print(p) # 1
p = list.pop(0)
print(p) # 7

# 요소 포함 여부
print(2 in list) # True

# 포함된 요소 개수
c = list.count(2)
print(c) # 1

# 확장
list.extend([8,9])
print(list) # [6,5,2,8,9]

# 특정요소 모두 제거
list = [1,2,3,3,3,3,5,5,5]
remove_set = {3,5}
result = [i for i in list if i not in remove_set]
print(result) #[1, 2]

# 문자열로 변환
list = ['1', '2', '3']
print(''.join(list))

# unshift
list = [1, 2, 3]
list.insert(0, 0)
print(list) # 0, 1, 2, 3

# shift
list = [1, 2, 3]
list.pop(0)
print(list) # 2, 3

# push
list = [1, 2]
list.append(3)
print(list) # 1, 2, 3

# pop
list = [1, 2, 3]
list.pop()
print(list) # 1, 2