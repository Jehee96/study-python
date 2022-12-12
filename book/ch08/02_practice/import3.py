# 8.1.2) import에 대해
# import의 역할은 정확하게는 '다른 모듈 내의 코드에 대한 접근'을 가능하게 하는 것이다.
# import가 접근 가능하게 하는 코드에는 변수, 함수, 클래스 등이 모두 포함된다.
# import를 사용하는 방법은 두 가지가 있다. 다음과 같이 import 뒤에 모듈명을 붙이는 것이다. 이때 확장자 '.py'는 제외해야 한다.

# import 모듈  # 모듈의 실제 파일 명은 "모듈.py"

# import문을 사용하는 두 번째 방법은 다음과 같은 꼴로 'from절'과 함께 사용하는 것이다.
# from절 뒤에 모듈이 따라오고, import 뒤에 변수 또는 함수가 따라온다.
# import문만 독단적으로 사용했을 때는 import뒤에 모듈 이름이 따라오던 것과는 다른 모습이다.

# from 모듈
import calculator1

print(calculator1.plus(10, 5))     
print(calculator1.minus(10, 5))     
print(calculator1.multiply(10, 5))  
print(calculator1.divide(10, 5))

# from 모듈 import 변수 또는 함수
from calculator1 import plus
from calculator1 import minus
from calculator1 import multiply
from calculator1 import divide

print(plus(10, 5))
print(minus(10, 5))
print(multiply(10, 5))
print(divide(10, 5))

# 위 두 가지 스타일 사이에 우열 같은 것은 없다. 상황에 따라 적절하게 선택해서 사용하면 된다.
# >>> calc_tester
