# 함수의 결과로써 함수를 반환할 수 있다.
def hello_korean():
    print('안녕하세요.')
    
def hello_english():
    print('Hello.')
    
def get_greeting(where):
    if where == 'K':
        return hello_korean   # 매개변수 where가 'K'인 경우 hello_korean() 함수를 반환한다.
    else:
        return hello_english  # 그 외의 경우 hello_english() 함수를 반환한다.
    

hello = get_greeting('K')     # get_greeting() 함수가 반환하는 결과를 변수 hello에 담아 '호출'한다.
hello()
# 안녕하세요.

hello = get_greeting('E')
hello()
# Hello.
