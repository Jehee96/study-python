# 한 함수 안에 return문을 여러 개 두는 것이 문법적인 문제를 일으키지는 않지만
# 가급적 return문은 함수 코드블록의 마지막에 하나만 실행하도록 하는 것이 좋다.
# 이번 예제 코드에는 my_abs() 함수를 조금 수정한 버전이다.
# 이 함수는 매개변수로 0을 입력받으면 아무것도 반환하지 않은 채로 실행을 종료한다.
# 이런 함수는 호출자에게 None Type의 None값을 반환한다.
def my_abs(arg):
    if arg < 0:
        return arg * -1
    elif arg < 0:
        return arg
    
result = my_abs(-1)
print(result)  # 1

result = my_abs(1)
print(result)  # None

result = my_abs(0)
print(result)  # None

print(result == None)  # True
print(type(result))    # <class 'NoneType'>

# 이번 예제 코드는 'return문에 아무 결과도 넣지 않고 실행하기'이다.
# 이 방식의 return문은 호출자에게 '반환'한다기보다는 함수를 '종료'시키는 용도로 사용된다.
# 이 예제 코드에서는 ogamdo() 라는 함수가 입력받은 횟수만큼 for 반복문을 실행하려고 시도하나,
# 다섯 번째 반복을 수행한 후에 return문에 의해 종료되고 만다.
def ogamdo(num):
    for i in range(1, num+1):
        print('제 {0}의 아해'.format(i))
        if i == 5:
            return  # 반환할 데이터 없이 실행하는 return문은 '반환'의 의미보다는 '함수 종료'의 의미로 사용된다.
        
print(ogamdo(3))  # 제 1의 아해
                  # 제 2의 아해
                  # 제 3의 아해
                  
print(ogamdo(5))  # 제 1의 아해       
                  # 제 2의 아해
                  # 제 3의 아해
                  # 제 4의 아해
                  # 제 5의 아해
                  
print(ogamdo(8))  # for 반복문응 8번 반복을 수행하려고 하지만, 실행되는 return문 때문에 다섯 번 수행하면 함수가 종료된다.

# 마지막으로, return문을 굳이 쓸 필요가 없다면 생략할 수 있다.
def print_something(*args):  # 반환할 결과도 없고, 함수를 중간에 종료시킬 일도 없다면 return문은 생략해도 된다.
    for s in args:
        print(s)
        
print(print_something(1, 2, 3, 4, 5))  # 1
                                       # 2
                                       # 3
                                       # 4
                                       # 5
