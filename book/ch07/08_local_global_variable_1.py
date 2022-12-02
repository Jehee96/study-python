# 7.5) 함수 밖의 변수, 함수 안의 변수 : 지역 변수(Local Variable)
# Questions
# "함수 밖에서 변수 a를 정의해 0을 대입하고, 함수 안에서 변수 a를 또 정의해 1을 대입했다. 이 함수를 실행(호출)하면 함수 밖에서 정의된 변수의 a값은?"

# Answer
def scope_test():
    a = 1                     # 함수를 정의하는 시점에서는 a가 메모리에 생성되지 않는다.
    print('a:{0}'.format(a))  # 함수를 '호출'하면 그제서야 함수의 코드가 실행되면서 a가 메모리에 생성된다.
    
    
a = 0                         # 함수 밖에서 a를 정의하고 '0으로' 초기화한다.
scope_test()                  # scope_test()가 호출되면 함수 내부에서 a를 정의하고 '1로' 초기화한다.
# a:1

print('a:{0}'.format(a))      # 하지만 함수 밖에서 정의한 a를 출력해보면 여전히 0을 갖고 있음을 확인할 수 있다.
# a:0

# 정답은 '0'이다. 함수 밖에 있는 a와 안에 있는 a는 이름은 같지만 완전히 별개의 변수이다.
# 이 현상을 이해하려면 변수의 유효 범위(Scope)라는 개념을 알아야 한다.
# 변수는 자신이 생성된 범위(코드블록) 안에서만 유효하며, 함수 안에서 만든 변수는 함수 안에서만 살아있다가 함수 코드의 실행이 종료되면 그 생명을 다한다.
# 이것을 '지역 변수(Local Variable)'라고 한다.
