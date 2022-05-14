arr = [1,2,3,4,5]

def add(x):
    return x + 1

arr = map(add, arr)
for a in arr:
    print(a, end=' ')

# 결과
# 2 3 4 5 6