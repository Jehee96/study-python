# 4.4) 수에서 텍스트로, 텍스트에서 수로
# 내장함수 input() 은 사용자로부터 입력을 받아들여 프로그램에 전달한다. 전달하는 데이터의 형식은 '문자열'이다.
# input() 함수는 문자열을 전달. 하지만 문자열끼리는 '*' 연산자로 곱셈을 수행할 수 없다.

# a = input("첫 번째 수를 입력하세요. : ")
# b = input("두 번째 수를 입력하세요. : ")

# result = int(a) * int(b)

# print("{0} * {1} = {2}".format(a, b, result))


# 숫자형식 > 문자열로 변환하는 예제
import math

print(type(math.pi))
text = input("원주율은" + str(math.pi) + "입니다.")
print(text)