# 7.8) 함수 안의 함수 : 중첩 함수
# 파이썬에서는 함수 안에 함수를 정의하는 것이 가능하다. 이것을 '중첩 함수(Nested Function)'라고 한다.
# 이 중첩 함수는 자신이 소속된 함수의 매개변수에 접근할 수 있다는 특징이 있다.
# 다음은 중첩 함수의 예제 코드이다. 이 예제 코드에서 stddev()는 표준 편차를 구하는 함수인데 mean()과 variance()를 중첩 함수로 갖고 있다.
# mean()과 variance()는 중첩 함수의 특징을 활용하여 stddev()의 매개변수인 args에 접근해서 평균과 분산을 각각 계산한다.

import math

# standard deviation : 표준 편차
def stddev(*args):

    # mean : 평균
    def mean():
        return sum(args)/len(args)

    # variance : 분산
    def variance(m):
        total = 0
        for arg in args:
            total += (arg - m) ** 2
        return total / (len(args) -1)

    v = variance(mean())
    
    return math.sqrt(v)

print("표준편차는 %0.1f입니다." % stddev(2.3, 1.7, 1.4, 0.7, 1.9))

# 중첩함수의 또 다른 특징은 자신이 소속되어 있는 함수 외부에서는 보이지 않는다는 것이다.
# 조금 전 예제 코드에서 stddev() 함수 안에서 정의한 mean() 함수를 호출하려고 하면 파이썬은 다음과 같이 해당 함수가 정의되지 않았다는 오류 메시지를 출력한다.
# print(mean())
# Traceback (most recent call last):
#   File "c:/Workstation/JJ/study-python/book/ch07/11_nested_function.py", line 31, in <module>
    # print(mean())
# NameError: name 'mean' is not defined
