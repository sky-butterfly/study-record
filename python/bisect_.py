from bisect import bisect_left, bisect_right

l = [1, 2, 3, 4, 5]
x = 3

print(bisect_left(l, x))
print(bisect_right(l, x))

# 정렬된 리스트에서 원소 개수 구하기

print(bisect_right(l, x)-bisect_left(l, x))