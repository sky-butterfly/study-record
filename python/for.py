# 리스트 역순으로 순회
list = [1, 2, 3]
for l in reversed(list):
  print(l, end=' ')
print()
# 3 2 1

# 숫자 범위 역순으로 순회
number = 10
for i in range(3, 0, -1):
  print(i, end=' ')
print()
# 3, 2, 1

# list 를 순회하면서 index 값 얻기
list = [1, 2, 3]
for i, v in enumerate(list, 0): # enumerate(리스트, 순회 시작할 인덱스)
  print(i, v, end=',') # 0 1, 1 2, 2 3,
print()