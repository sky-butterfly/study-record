# 타입확인

# type()
print(type(1))
print(type(1.1))
print(type('s'))
print(type([1,2,3]))

# print result
# <class 'int'>
# <class 'float'>
# <class 'str'>
# <class 'list'>

# 조건문에서 타입 체크
if type(1) is int:
    print('int')
if type(1.1) is float:
    print('float')
if type('s') is str:
    print('str')
if type([1,2,3]) is list:
    print('list')

# isinstance()
print(isinstance(1, int))
print(isinstance(1.1, float))
print(isinstance('s', str))
print(isinstance([1,2,3], list))

# result
# True
# True
# True
# True

# 조건문에서 타입 체크
if isinstance(1, int):
    print('int True')