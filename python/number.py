import fractions

# 숫자를 문자형으로 변환
n = 100
print(str(n))
print(repr(n))

# 절대값
n = -1
print(abs(n)) # 1

# 제곱근
n = 4
print(int(4 ** 0.5)) # 2

# 정수 판별
n = 5
print(n % 1 == 0) # True

# 숫자인지 판별
n = "1"
print(n.isdigit()) # True

# 이진수 변환 ( 10진수 -> 2진수 )
n = 55
print(bin(n)) # 0b110111

# 이진수 변환 ( 2진수 문자열 -> 10진수 )
s = '10'
print(int(s, 2)) # 2

# 이진수 변환 ( 10진수 -> 2진수 접두어 제외)
n = 55
print(format(n, 'b')) # 110111

# 2의 거듭제곱인지 확인
# 2의 거듭제곱인 n을 비트로 나타낼 때, 가장 왼쪽만 1이며, n-1 은 가장 왼쪽은 0, 나머지는 모두 1이 된다. 따라서 n 과 n-1 을 &(and) 연산하면 결과는 0이 나온다.
n = 8
print(n&(n-1) == 0) # True

# 기약분수
# import fractions
a, b = 2, 4
x = fractions.Fraction(a, b)
print(x) # 1/2

# 기약분수 분자
print(x.numerator) # 1
# 기약분수 분모
print(x.denominator) # 2

# 2진수, 8진수, 16진수
print(bin(4))
print(oct(4))
print(hex(4))