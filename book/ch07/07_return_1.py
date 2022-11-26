# 7.4) 호출자에게 반환하기
# 함수가 호출자에게 값을 반환할 때에는 return문이 이용된다. return문은 대체로 다음 세 가지 방법으로 사용된다.

# 1. return문에 결과 데이터를 담아 실행하기 -> 함수가 즉시 종료되고 호출자에게 결과가 전달된다.
# 2. return문에 아무 결과도 넣지 않고 실행하기 -> 함수가 즉시 종료된다.
# 3. return문 생략하기 -> 함수의 모든 코드가 실행되면 종료된다.

# 'return문에 결과 데이터를 담아 실행하기' 예제 코드이다.
def multiply(a, b):
    return a*b  # return문은 함수의 실행을 종료시키고 자신에게 넘겨진 데이터를 호출자에게 전달한다.

result = multiply(2, 3)
print(result)   # 6

# 한 함수 안에 여러 개의 return을 배치하는 것도 가능하다.
# 다음은 앞에서 만든 my_abs() 함수 안에 두 개의 return문을 사용하도록 수정한 예제 코드이다.
def my_abs(arg):
    if arg < 0:
        return arg * -1
    else:
        return arg

result = my_abs(-1)
print(result)  # 1

result = my_abs(1)
print(result)  # 1
