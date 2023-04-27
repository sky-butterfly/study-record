# 문자열을 리스트로 바꾸기
str = 'string'
l = list(str)
print(l)
# 결과 ['s', 't', 'r', 'i', 'n', 'g']

# 특정 문자열 제거
# strip : 양 끝의 문자 제거
str = 'aaaaaaHello Worldaaaa'
print(str.strip('a')) # Hello World

# lstrip : 왼 쪽 끝의 문자 제거
str = 'iiiiiiHello World'
print(str.lstrip('i')) # iiiiiiHello World
print(str) # Hello World

# rstrip : 오른쪽 끝의 문자 제거
str = 'Hello Worldbbbbb'
print(str.rstrip('b')) # Hello World
print(str) # Hellow Worldbbbbb

# 문자열 치환
str = 'aaabbbccc'
print(str.replace('b', '')) # aaaccc
print(str) # aaabbbccc

# translate 여러 개 문자열 제거
str = 'abc'
newStr = str.maketrans({
    'a' : 'd',
    'b' : 'e',
    'c' : 'f'
})
print(str.translate(newStr)) # def
print(str) # abc

# 문자열 길이
print(len('abc')) # 3

# 대문자 변환
str = 'h'
print(str.upper()) # H

# 소문자 변환
str = 'H'
print(str.lower()) # h

# 대문자 여부
str = 'H'
print(str.isupper()) # True

# 소문자 여부
str = 'h'
print(str.islower()) # True

# 문자열 연결
arr = ['a', 'b', 'c']
str = ''
for a in arr:
    str = str + a
print(str) # abc

# 문자열 연결 (join 함수 활용)
arr = ['a', 'b', 'c']
print(''.join(arr)) # abc

# 인덱스로 문자열 추출
str = 'Hello World!';
print(str[2]) # l
print(str[1:2]) # e
print(str[:]) # Hello World!
print(str[1:]) # ello World!
print(str[-2:]) # d!

# 문자열 길이
str = '12345'
print(len(str))

# 정수로 변환
str = 100
print(int(str))