# 6.1.5) 비교 연산자
# 앞의 예제에서 등장한 '==' 기호는 두 피연산자가 '동등한지'를 평가(Evaluation) 하는 연산자다.
# 두 연산자가 같으면 True, 아니면 False의 결과를 내놓는다.
# == 연산자처럼 두 피연산자를 비교하는 연산자를 '비교 연산자'라고 하는데 파이썬에서는 6가지의 비교 연산자가 있다.

# == /양쪽에 위치한 피연산자가 서로 '같으면' True, 그렇지 않으면 False이다.
a = 30
print(a == 30)  # >> True
print(a == 40)  # >> False
print(a == 2)   # >> False

# != /양쪽에 위치한 피연산자가 서로 '다르면' True, 그렇지 않으면 False이다.
a = '안녕'
print(a != '안녕')   # >> False
print(a != 'Hello')  # >> True

# >  /왼쪽에 위치한 피연산자가 오른쪽 피연산자보다 '크면' True, 그렇지 않으면 False이다.
a = 30
print(a > 20)  # >> True
print(a > 40)  # >> False

# >= /왼쪽에 위치한 피연산자가 오른쪽 피연산자보다 '크거나 같으면' True, 그렇지 않으면 False이다.
a = 30
print(a >= 20)  # >> True
print(a >= 30)  # >> True
print(a >= 40)  # >> False

# <  /왼쪽에 위치한 피연산자가 오른쪽 피연산자보다 '작으면' True, 그렇지 않으면 False이다.
a = 30
print(a < 40)  # >> True
print(a < 20)  # >> False

# <= /왼쪽에 위치한 피연산자가 오른쪽 피연산자보다 '작거나 같으면' True, 그렇지 않으면 False이다.
a = 30
print(a <= 40)  # >> True
print(a <= 30)  # >> True
print(a <= 20)  # >> False
