from itertools import permutations, combinations, product, combinations_with_replacement

# 순열
l = [1, 2, 3]
print(list(permutations(l, 2)))

# 조합
print(list(combinations(l, 2)))

# 중복순열
print(list(product(l, repeat=2)))

# 중복조합
print(list(combinations_with_replacement(l, 2)))