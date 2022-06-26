# 정수, 실수, 복소수, 문자열, 리스트, 튜플, 사전 등
# 리스트는 자바의 ArrayList의 특징을 가지고 있음

# 정수형, 실수형이 가장 많이 사용함
# 양의 정수
a = 1000
print(a)

# 음의 정수
a = -7
print(a)

# 0
a = 0
print(a)

a = 777
a = a + 5
print(a)

# 실수형
a = 157.95
print(a)

a = -1992.35
print(a)

a = 1e9
print(a)

a =75.25e1
print(a)

a = 345.4e-2
print(a)

# 실수는 오차가 있다.
a = 0.3 + 0.6
print(a)
print(type(a))

a = 7
b = 3
print(a/b)  # c나 java는 정수형 연산의 경우 몫만 정수형으로 표현

print(a%b)
print(a//b)

print(3**2)   # 제곱
print(4**0.5) # 제곱근