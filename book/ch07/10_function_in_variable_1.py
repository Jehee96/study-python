# 7.7) 함수를 변수에 담아 사용하기
# 파이썬에서는 함수를 변수에 담아 사용할 수 있다.
def print_something(a):
    print(a)
    
    
p = print_something    # ()없이 함수의 이름만을 변수에 저장한다.
p(123)                 # 변수의 이름 뒤에 ()를 붙여 함수처럼 호출한다.
# 123

p('abc')
# abc

# 함수를 변수처럼 사용할 수 있듯이, 순서열이나 딕셔너리에도 담을 수 있다.
def plus(a, b):
    return a+b

def minus(a ,b):
    return a-b

flist = [plus, minus]  # plus() 함수와 minus() 함수를 리스트의 요소로 집어넣는다.
print(flist[0](1, 2))  # flist[0]은 plus() 함수를 담고 있다. 따라서 이 요소 뒤에 괄호를 열고 매개변수를 입력하여 호출하면 plus() 함수가 호출된다.
# 3

print(flist[1](1,2))
# -1                   # flist[1]은 minus()를 담고 있으므로 이 코드는 minus(1, 2)와 같다.

# 파이썬에서는 함수를 다른 함수의 매개변수로 사용할 수 있다. 다음은 함수를 매개변수로 사용하는 예제 코드이다.
def hello_korean():
    print('안녕하세요.')
    
def hello_english():
    print('Hello.')
    
def greet(hello):
    hello()            # 입력받은 매개변수 hello 뒤에 괄호()를 붙여 호출한다.
                       # 함수를 정의하는 시점에서는 hello가 함수인지 매개변수의 수가 맞는지 등은 파이썬이 검사하지 않는다.
    
greet(hello_korean)    # greet() 함수에 hello_korean() 함수를 매개변수로 넘겨 호출한다.
# 안녕하세요.

greet(hello_english)   # greet() 함수에 hello_english() 함수를 매개변수로 넘겨 호출한다.
# Hello.
