# 5.2.2) 튜플 메소드
# 튜플은 변형이 불가능한 자료형이며, 제공하는 메소드는 index(), count() 두 개 뿐이다.

# index() /매개변수로 입력한 데이터와 일치하는 튜플 내 요소의 첨자를 알려준다. (n번째 위치 알려줌)
# 찾고자 하는 데이터와 일치하는 요소가 없으면 오류를 일으킨다.
a = ('abc', 'def', 'ghi')
print(a.index('ghi'))  # >> 2
try:
    print(a.index('jkl'))  # >> ValueError: tuple.index(x): x not in tuple
except ValueError:
    print('ValueError: tuple.index(x): x not in tuple')

# count() /매개변수로 입력한 데이터와 일치하는 요소가 몇 개 있는지 센다.
a = (1, 100, 2, 100, 3, 100)
print(a.count(100))  # >> 3
print(a.count(200))  # >> 0