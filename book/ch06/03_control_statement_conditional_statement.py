# 6.1.3) 흐름 제어문과 조건문
# 흐름 제어문은 흐름을 분기하거나 반복하기 전에 조건문의 결과가 참인지를 평가한다.
# 이 조건문은 bool 형식을 비롯해 숫자, 문자열, 딕셔너리 등 다양한 객체가 사용된다.
# 조건문이 구체적으로 다음과 같을 때 '거짓'으로 평가된다.

# False
# None
# 숫자 0 :  ex) 0, 0.0 등
# 비어있는 순서열 : ex) '', (), [] 등
# 비어있는 딕셔너리 : ex) {}

# 어떤 객체가 거짓으로 평가되는지를 알고 싶을 때는 bool() 함수를 이용할 수 있다.
print(bool(False))      # >> False
print(bool(None))       # >> False
print(bool(0))          # >> False
print(bool(0.0))        # >> False
print(bool(''))         # >> False
print(bool('Hello'))    # >> True
print(bool(123))        # >> True
print(bool(()))         # >> False
print(bool([]))         # >> False
print(bool([1, 2, 3]))  # >> True
print(bool({}))         # >> False
