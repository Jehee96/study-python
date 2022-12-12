# 8.1.1) 두 개의 소스 파일로 만드는 하나의 프로그램 예제_2
# 02. calc_tester.py

import calculator1                  # 불러올 모듈의 이름에서 '.py'는 생략한다.

print(calculator1.plus(10, 5))      # 15
print(calculator1.minus(10, 5))     # 5
print(calculator1.multiply(10, 5))  # 50
print(calculator1.divide(10, 5))    # 2.0
# 모듈이름.함수()의 꼴로 calculator모듈의 함수를 호출한다.
# 디렉토리를 하나 골라 저장 후, 명령 프롬프트를 열어 실행하면 결과를 확인할 수 있다.

# calc_tester.py는 plus() 함수나 minus() 함수 따위를 구현하고 있지 않다. 이 함수들은 모두 calculator.py 모듈에 정의되어 있다.
# calc_tester.py 모듈에서 'import문'을 이용해 calculator.py 모듈을 불러들였기 때문에 이들 함수를 사용할 수 있었고,
# 이렇게 모듈을 분리함으로써 얻는 또 하나의 장점은 코드를 '재사용'할 수 있다고 말할 수 있다.
# import가 별 것 아닌 것처럼 보여도 모듈과 모듈을 결합하는 중요한 역할을 한다.

# 한편, 'from 모듈 import 변수 또는 함수' 스타일은 또 다시 세 가지 버전으로 나뉜다.
# 첫 번째로는 다음 예제 코드와 같이 사용할 변수나 함수의 이름을 일일이 명기해주는 방식이다.
# calc_tester2.py

from calculator1 import plus      
from calculator1 import minus

print(plus(10, 5))                # calculator 모듈의 plus라는 함수를 불러들였으므로 'calculator'없이 plus() 이름만으로 함수를 호출할 수 있다.
print(minus(10, 5))
# print(multiply(10, 5))          # multiply()와 divide()는 import하지 않았다. 현재 모듈에서는 보이지 않는 함수다.
# print(divide(10, 5))

# 두 번째로는 변수 또는 함수 이름을 명기하는 방식이지만 콤마(,)를 이용해서 여러 함수(또는 변수)의 이름을 한 줄에 넣는 스타일이다.
# calc_tester3.py

from calculator1 import plus, minus
                                  # from calculator1 import plus, from calculator1 import minus와 동일한 코드이다.
print(plus(10, 5))
print(minus(10, 5))
# print(multiply(10, 5))
# print(divide(10, 5))

# 세 번째 방식. 이도 저도 귀찮으면 다음과 같이 와일드카드(*)를 이용할 수도 있다.
# calc_tester4.py

from calculator1 import*

print(plus(10, 5))                
print(minus(10, 5))
print(multiply(10, 5))          
print(divide(10, 5))
# 그러나 import*와 같은 코드는 사용하지 않는 것이 좋다.
# 코드가 복잡해지고 모듈의 수가 많아지면 저런 코드가 어떤 모듈 또는 어떤 변수, 함수를 불로오고 있는지 파악하기 힘들어진다.
# 다시 말해 코드를 읽는데 상당한 지장을 준다.
# import문을 이용해 모듈에 접근할 때에는 불러올 변수, 함수의 이름을 정확하게 명시하는 것을 권한다.

# "import calculator" 코드를 통해 모듈을 불러와서 calculator 안에 정의되어 있는 함수를 호출할 때,
# calculator라는 모듈 이름을 일일이 입력하기가 너무 귀찮은데 이 귀찮음을 해결할 수 있는 'as' 키워드가 있다.
# 'as' 키워드는 'import 모듈 as 새이름'의 꼴로 사용하면 된다. 다음은 예제 코드이다.
# calc_tester5.py

import calculator1 as c  # calculator 모듈을 c라는 이름으로 불러온다.

print(c.plus(10, 5))     # calculator라는 이름 대신 c를 이용해 함수 이름에 접근한다.
print(c.minus(10, 5))
print(c.multiply(10, 5))
print(c.divide(10, 5))