# 5.3) 딕셔너리
# 사용법 측면으로는 리스트와 비슷하다. 리스트처럼 첨자를 이용해 요소에 접근하고, 그 요소를 변경할 수 있다.
# 둘의 차이점은 '리스트'는 요소에 접근할 때 0부터 시작하는 수 첨자만 사용이 가능하지만,
#               '딕셔너리'는 문자열과 숫자를 비롯해 변경이 불가능한 형식이면 어떤 자료형이든 사용이 가능하다.
# 딕시녀리의 첨자는 키(Key)라고 하고, 이 키가 가리키는 슬롯에 저장되는 데이터를 일컬어 값(Value)라고 한다. (키-값의 쌍으로 구성)
# 딕셔너리를 만들 때는 중괄호{와 }을 이용한다.
# 특정 슬롯에 새로운 키-값을 입력하거나 딕셔너리 안에 있는 요소를 참조할 때는 리스트와 튜플에서처럼 대괄호[와 ]를 이용한다.
dic = {}
dic['파이썬'] = 'www.python.org'
dic['마이크로소프트'] = 'www.microsoft.com'
dic['애플'] = 'www.apple.com'
print(dic['파이썬'])          # >> www.python.org
print(dic['마이크로소프트'])  # >> www.microsoft.com
print(dic['애플'])            # >> www.apple.com
print(type(dic))              # >> <class 'dict'>

# 배열과 다른 점이라면 배열이 데이터를 저장할 요소의 위치로 인덱스를 사용하는 반면에, 딕셔너리는 키 데이터를 그대로 사용한다.
# 키를 이용해서 단번에 데이터가 저장된 위치의 주소를 계산하기 때문인데 이 작업을 해싱(Hashing)이라고 한다.
# 변경이 '불가능한' 자료형에 대해서만 해싱을 할 수 있기 때문에 변경이 가능한 자료형은 딕셔너리의 키로 사용할 수 없다.

# 딕셔너리가 제공하는 메소드
# 딕셔너리는 자신에게 저장되어 있는 '키의 목록'과 '값의 목록'을 따로 추려낼 수 있다.
# key()는 키의 목록을, values()는 값의 목록을 추려낸다.
print(dic.keys())    # >> dict_keys(['파이썬', '마이크로소프트', '애플'])
print(dic.values())  # >> dict_values(['www.python.org', 'www.microsoft.com', 'www.apple.com'])

# 딕셔너리의 items() 메소드는 키와 값의 쌍으로 이루어진 '전체 목록'을 반환한다.
print(dic.items())  # >> dict_items([('파이썬', 'www.python.org'), ('마이크로소프트', 'www.microsoft.com'), ('애플', 'www.apple.com')])

# in 연산자를 이용하면 특정 키가 목록 안에 존재하는지 확인할 수 있다. 값에 대해서도 마찬가지이다.
print('애플' in dic.keys())                 # >> True
print('사과' in dic.keys())                 # >> False
print('www.microsoft.com' in dic.values())  # >> True
print('www,seanlab.net' in dic.values())    # >> False

# 딕셔너리 안에 있는 키-값 쌍을 제거하려면 pop() 메소드를 이용한다.
# pop() 메소드의 매개변수로는 삭제할 키-값 쌍의 키를 입력한다.
dic = {'애플': 'www.apple.com', '파이썬': 'www.python.org', '마이크로소프트': 'www.microsoft.com'}
dic.pop('애플')  # >> www.apple.com /키가 '애플'인 요소를 삭제한다.
print(dic)       # >> {'파이썬': 'www.python.org', '마이크로소프트': 'www.microsoft.com'}

# 딕셔너리의 데이터를 남김없이 정리하고자 할 때는 clear() 메소드를 사용한다.
dic.clear()
print(dic)  # >> {}