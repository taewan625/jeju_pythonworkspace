# 비교 연산자 같다==, 같지않다 !=, >, ,< =<, =>
# 논리연산자: 논리곱, 교집합 and, & 논리합, 합집합 or (긴짝대기 ?)
# not 반전 True <-> False

# type()
f = 3.14
print(type(f)) # class float: 실수형
i = 2354
print(type(i)) # int
s = "python"
print(type(s)) # string
g = True
print(type(g)) # bool
b = False
print(type(b))

# 숫자형 -> 문자형
a = 100
print(type(a)) # int
print(type(str(a))) # str

# 문자형 -> 숫자형
int()
print(type(int(a)))
