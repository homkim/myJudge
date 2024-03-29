
# 정수, 실수, 복소수, 문자열, 리스트, 튜플, 사전 등
# 리스트는 자바의 ArrayList의 특징을 가지고 있음

'''

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


'''

'''
# 리스트 자료형: 자바의 어레이리스트와 유사. 단순히 배열이라고 생각하면 됨
arr = [1,2,3,4]
print(arr)

print(arr[3])

n = 10
arr = [0]*n  # 배열의 선언 및 초기화
print(arr)

# 인덱싱과 슬라이싱
arr = [1,2,3,4]
print(arr[1:4])  # Range 및 슬라이싱의 오른쪽은 원하는값 +1을 해줘야 함

arr = [i+1 for i in range(10)]
print(arr)

for i in range(10):
    print(i, end=' ')
print('')

'''

""" 
for _ in range(5):
    print("Hello World")

arr = [4, 3, 1,2]    

arr.append(5)
print(arr)

arr.sort()
print(arr)
arr.reverse()
print(arr)
arr.insert(2, 7)
print(arr)

arr.remove(1)
print(arr)

a = [1,2,3,4,5,5,5,]
remove_set = {3, 5} # 집합 자료형

result = [ i for i in a if i not in remove_set]
print(result)
 """

# 문자열 자료형
str = 'Hello World' 
print(str)

str = 'Do you know "Python"?'
print(str)

# str[4] = 'a'  # 불가

# 튜플
a = (1,2,3,4)
print(a[3])
