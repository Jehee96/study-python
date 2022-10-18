# 5.2.1) 패킹과 언패킹
# 아래와 같이 여러 가지 데이터를 튜플로 묶는 것을 튜플 패킹(Tuple Packing)이라고 한다.
a = 1, 2, 3
print(a)  # >> (1, 2, 3)

# 그리고 다음과 같이 튜플의 각 요소를 여러 개의 변수에 할당하는 것을 튜플 언패킹(Tuple Unpacking)이라고 한다.
one, two, three = a
print(one)    # >> 1
print(two)    # >> 2
print(three)  # >> 3

# 튜플 언패킹을 할 때에는 튜플 요소의 수와 각 요소를 담아낼 변수의 수가 일치해야 한다. (a, b, c), (1, 2, 3)
# 이 조건을 만족하지 못하면 파이썬 인터프리터는 다음과 같이 오류 메시지를 출력한다.
# one, two = a
# Traceback (most recent call last):
#   File "c:/Workstation/JJ/study-python/ch05/04_tuple_packing_tuple_unpacking.py", line 14, in <module>
#     one, two = a
# ValueError: too many values to unpack (expected 2)

# 튜플 언패킹을 활용하려면 다음과 같이 여러 개의 변수에 한번에 할당을 수행할 수 있다.
city, latitude, longitude = 'Seoul', 37.541, 126.986
print(city)       # >> 'Seoul'
print(latitude)   # >> 37.541
print(longitude)  # >> 126.986