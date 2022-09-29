# 4.2.4) math 모듈을 이용한 계산

# math 모듈이란? 여러 가지 수학 함수를 담고 있는 모듈이다.
# 모듈을 사용하려면 import 구문을 이용한다.
import math

# π와 e
# math 모듈에는 원주율 π와 자연상수 e의 정의가 되어있다.

print(math.pi)
# >>> 3.141592653589793
print(math.e)
# >>> 2.718281828459045

# 파이썬 코드에서 '.'은 '~의'로 해석하면 코드를 읽기가 좋다.
# ex) math.pi = math(모듈)의 pi

# 두 상수는 무한 소수이지만 파이썬의 float타입으로 정의되어있다.
# 이렇게 해야 float 자료형을 사용하는 다른 함수와 사용이 가능하다.


# 절대값, 버림과 반올림
# abs() = 절대값 계산 함수, round() 반올림 계산 함수, trunc() 버림 계산 함수
# abs(), round() 함수는 내장 함수(Built-in function). 별도의 import 구문을 통하지 않고 바로 사용 가능.
# trunc() 함수는 math 모듈안에 들어있으므로 import 구문을 이용해야 사용 가능.

print(abs(10))
print(abs(-10))

print(round(27.6))

# trunc() 함수는 1.4, 1.5, 1.9를 모두 1로 만든다.
# trunc() 함수는 앞의 두 함수와 달리 내장 함수가 아니므로 사용할 때 'math'를 앞에 붙인다.

import math
print(math.trunc(1.4))
print(math.trunc(1.5))
print(math.trunc(1.9))
print(math.trunc(23.8))
print(math.trunc(27.5465468487465))

# 팩토리얼
# 팩토리얼은 1부터 어떤 양의 정수 n까지의 정수를 모두 곱한 것이다.
# ex) 5 팩토리얼 수식 = 5! = 5x4x3x2x1
# math 모듈에서 제공하는 팩토리얼 함수의 이름은 factorial()이다.

# factorial() 함수는 정수를 매개변수로 받는다.
print(math.factorial(23))
print(math.factorial(27))

# 도와 라디안
# 도(degree)는 원을 360도로 표현한 것이고, 라디안(radian)은 반지름이 1인 원에서 호의 길이가 1인 부채꼴의 각을 기본 단위로 삼아 2π로 표현한 것이다.
# 즉, 360도 = 2π인 것이다. math 모듈은 다음과 같이 도와 라디안 사이의 단위 변환을 계산하는 함수로 이를 제공한다.

# degrees() = 라디안을 입력받아 도를 계산
# radians() = 도를 입력받아 라디안을 계산

import math
print(math.degrees(math.pi))
print(math.degrees(math.pi/2))

print(math.radians(180))
print(math.radians(90))

# 삼각 함수
# 다음은 math 모듈에서 제공하는 삼각 함수의 목록을 보여준다.
# cos() = 입력된 라디안에 대한 코사인 값을 계산.
# sin() = 입력된 라디안에 대한 사인 값을 계산.
# tan() = 입력된 라디안에 대한 탄젠트 값을 계산.

# acos() = cos()의 역함수
# asin() = sin()의 역함수
# atan() = tan()의 역함수

# 위 삼각 함수의 입력값은 라디안 단위여야 한다.

# ex) 삼각 함수 예제
import math
print(math.sin(math.radians(90)))
print(math.cos(math.radians(180)))
print(math.tan(math.radians(45)))
# 도를 입력해서 삼각 함수를 구하고 싶을 때에는 radians() 함수를 이용한다.
print(math.tan(math.pi/4))
# math.pi 상수를 이용할 수도 있다.
print(math.acos(-1))
print(math.asin(1.0))
print(math.atan(10000))

# 제곱과 제곱근
# 3의 2승, 3의 3승은 곱셈 연산자를 이용하여 계산할 수 있다.
print(3*3)
print(3*3*3)

# 곱셈 연산자보다 **연산자나 pow() 함수를 이용하는 방법도 있다.
# math 모듈에는 제곱근을 계산하는 sqrt() 함수도 있다.

# ** = 제곱 연산
# pow() = **와 같음 (math 모듈)
# sqrt() = 제곱근 연산 (math 모듈)

# ex) **와 pow() 함수를 이용하여 계산.
print(3**3)
import math
print(math.pow(3,3))

# sqrt() 함수를 이용해서 제곱근 구하기.
print(math.sqrt(4))
print(math.sqrt(81))
print(math.sqrt(100))

# ☆ sqrt() 함수는 제곱근만을 계산한다. ☆
# 세제곱근, 네제곱근같은 경우 pow() 함수를 이용하여 계산한다.

print(27**(1/3))
#  >>> 3.0
print(math.pow(81, 0.5))
# >>> 9.0

# 로그 함수
# math 모듈에서 제공하는 로그를 구하는 함수는 몇 가지 있지만 주로 사용되는 두 가지는 다음과 같다.

# log() = 첫 번째 매개변수의 로그를 구한다. 두 번째 매개변수는 밑수이다. 두 번째 매개변수를 생략하면 밑수는 자연수e로 간주된다.
# log10() = 밑수가 10인 로그를 계산한다.

import math
print(math.log(4, 2))
print(math.log(math.e))

print(math.log(1000, 10))
print(math.log10(1000))
# math.log(1000, 10)과 math.log10(1000)은 모두 log10 1000을 계산한다.
# 이 예제는 10을 밑으로 하는 수를 계산하는 데에는 log(10) 함수가 적합함을 보여준다.