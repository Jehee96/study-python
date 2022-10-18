# 6.1.2) 논리 연산자
# not, and, or은 참과 거짓을 다루는 논리 연산자이다.
# not 연산자는 이름처럼 피연산자를 부정하는 결과를 낸다.
# 피연산자가 False인 경우에는 True, 그렇지 않은 경우에는 False를 출력한다.
print(not True)   # >> False
print(not False)  # >> True

# not 연산자는 bool 형식 외에도 수, 문자열, 튜플, 리스트, 딕셔너리도 피연산자로 사용이 가능하다.
# 입력된 피연산자가 0인 경우에는 피연산자를 '거짓'으로 간주하기 때문에 not 연산의 결과는 True가 된다.
# 0이 아닌 수를 피연산자로 사용하는 경우의 not 연산 결과는 False이다.
print(not 0)   # >> True
print(not -1)  # >> False
print(not 1)   # >> False

# 'None'에 대해서도 '거짓'으로 간주하기 때문에 not None의 결과는 다음과 같이 True가 된다.
print(not None)  # >> True

# not 연산자는 비어있는 문자열이나 튜플, 리스트, 딕셔너리도 '거짓'으로 간주한다.
# 따라서 '비어있는 상태의 문자열'이니 튜플, 리스트, 딕셔너리를 not 연산자에 피연산자로 입력하면 True, 그렇지 않으면 False의 결과가 나온다.
print(not 'ABC')      # >> False /비어있지 않은 문자열을 부정
print(not '')         # >> True /빈 문자열을 부정
print(not (1, 2, 3))  # >> False /비어있지 않은 튜플을 부정
print(not ())         # >> True /빈 튜플을 부정
print(not [])         # >> True /빈 리스트를 부정
print(not {})         # >> True /빈 딕셔너리를 부정

# and 연산자는 두 피연산자 간의 논리곱을 수행한다.
# 논리곱 연산의 결과는 두 피연산자 모두가 True인 경우에만 True가 되고 그렇지 않은 경우에는 항상 False가 된다.
print(True and True)   # >> True
print(True and False)  # >> False

# 반면 논리합을 수행하는 or 연산자는 두 피연산자가 모두가 False인 경우에만 False가 되고, 그렇지 않으면 항상 True가 된다.
# 즉, 피연산자 중 하나만 True면 결과도 True가 된다.
print(False or False)  # >> False
print(False or True)   # >> True
