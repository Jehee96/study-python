# 7.6) 자기 스스로를 호출하는 함수 : 재귀 함수
# 재귀 함수(Recursive Function)는 '자기 스스로를 호출'하는 함수를 말한다.
# 함수가 자기 자신을 부르는 것을 재귀 호출(Recursive Call)이라고 한다. 함수가 호출자이자 피호출자가 되는것이다.
# 다음은 재귀 함수의 간단한 예이다.
def some_func(count):
    if count > 0:
        some_func(count-1)
    print(count)
    
# 재귀 함수를 만드는데 알아야 하는 문법은 특별한 것이 없다. 그저 함수가 자기 자신을 호출하기만 하면 된다.
# 재귀 함수는 재귀 관계식(Recurrence relation, 점화식) 코드로 옮기고자 할 때 유용하다.
# 다음은 팩토리얼의 재귀 관계식이다.
def factorial(n):
    if n == 0:
        return 1
    elif n > 0:
        return factorial(n-1)*n
    
    
print(factorial(5))   # 120
print(factorial(10))  # 3628800
print(factorial(20))  # 2432902008176640000

# 재귀 함수는 편리하지만, 호출 비용이 크기 때문에 주의해야 한다.
# 컴퓨터가 더 많은 일을 하게 만들어서 성능이 떨어지는 소프트웨어를 만들게 한다.
# 때문에 좋은 성능이 요구되는 코드에서는 재귀 함수를 '반복문으로 대체'하는 것이 낫다.
# 또 하나 주의해야 할 점은 재귀 함수를 만들 때는 재귀 함수가 종료될 조건을 만들어줘야 한다.
# 그렇지 않으면 무한루프나 다름없는 코드가 되어버린다. 사실은 무한루프보다 더 나쁜 코드이다.
# 아무리 반복을 수행해도 메모리를 더 요구하지 않는 무한루프와는 달리 재귀 함수는 재귀 호출의 단계가 깊어질수록 메모리를 추가로 사용하기 때문이다.
# 다음은 종료조건이 없는 재귀 함수의 예제 코드이다.
def no_idea():
    print("나는 아무 생각이 없다.")
    print("왜냐하면")
    no_idea()  # 종료할 조건도 지정해주지 않은 채 무조건 재귀 호출을 수행하면 지속적으로 재귀 단계가 증가한다.
    

no_idea()
# 나는 아무 생각이 없다.
# 왜냐하면
# 나는 아무 생각이 없다.
# 왜냐하면
# 나는 아무 생각이 없다.
# 왜냐하면
# 나는 아무 생각이 없다.
# 왜냐하면
# 나는 아무 생각이 없다.
# …
# Traceback (most recent call last):
#   File "c:/Workstation/JJ/study-python/book/ch07/09_recursive_function.py", line 37, in <module>
    # no_idea()
#   File "c:/Workstation/JJ/study-python/book/ch07/09_recursive_function.py", line 34, in no_idea
    # no_idea()
# …
# File "c:/Workstation/JJ/study-python/book/ch07/09_recursive_function.py", line 32, in no_idea
    # print("나는 아무 생각이 없다.")
# RecursionError: maximum recursion depth exceeded while calling a Python object
# 재귀 단계가 파이썬에서 지정해 놓은 최대 재귀 단계를 초과하면서 파이썬은 에러를 일으키고 프로그램을 종료시킨다.
