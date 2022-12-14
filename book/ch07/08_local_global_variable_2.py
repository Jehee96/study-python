# 7.5) 함수 밖의 변수, 함수 안의 변수 : 전역 변수(Global Variable)
# 이와는 반대로 함수 외부에서 만든 변수는 프로그램이 살아있는 동안에는 함께 살아있다가 프로그램이 종료될 때 같이 소멸한다.
# 이렇게 '프로그램 전체'를 유효 번위로 가지는 변수를 '전역 변수(Global Variable)'라고 한다. 이 전역 변수는 '함수 또는 객체 사이에 데이터 교환이 필요할 때' 사용된다.
# 파이썬은 함수 안에서 사용되는 모든 변수를 '지역 변수로 간주'한다. 전역 변수를 사용하려면 global 키워드를 이용해야 한다.

# 다음은 전역 변수를 함수 안에서 접근하여 값을 수정하는 예제 코드이다.
def scope_test():
    global a                  # global 키워드는 지정한 변수의 유효 범위가 '전역'임을 알리고, 지역 변수의 생성을 막는다.
    a = 1                     # 이 a는 scope_test() 함수 안에서 전역 변수로 사용된다.
    print('a:{0}'.format(a))
    
    
a = 0
scope_test()                  # scope_test()는 0으로 초기화된 a에 접근해 1로 값을 변경한다.
# a:1

print('a:{0}'.format(a))      # a를 출력해보면 scope_test() 함수 안에서 변경한 값 1이 들어있음을 확인할 수 있다.
# a:1
