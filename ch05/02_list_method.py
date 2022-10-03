# 5.1.1) 리스트 메소드

# append() /리스트의 끝에 새 요소를 추가한다.
a = [1, 2, 3]
a.append(6)
print(a)  # >> [1, 2, 3, 6]

# extend() /기존 리스트에 다른 리스트를 이어 붙인다. + 연산자와 같은 기능을 한다.
a = [1, 2, 3]
a.extend([7, 8, 9])
print(a)  # >> [1, 2, 3, 7, 8, 9]

# insert() /첨자로 명시한 리스트 내의 위치에 새 요소를 삽입한다.
# insert(첨자, 데이터)의 형식으로 사용한다.
a = [2, 4, 5]
a.insert(0, 1)  # >> 0 위치(첫 번째)에 데이터 1을 삽입한다.
print(a)  # >> [1, 2, 4, 5]
a.insert(2, 3)  # >> 2 위치(세 번째)에 데이터 3을 삽입한다.
print(a)  # >> [1, 2, 3, 4, 5]

# remove() /매개변수로 입력한 데이터를 리스트에서 찾아 첫 번째 요소를 제거한다.
a = ['BMW', 'BENZ', 'VOLKSWAGEN', 'AUDI']
a.remove('BMW')
print(a)  # >> a = ['BENZ', 'VOLKSWAGEN', 'AUDI']

# pop() /리스트의 마지막 요소를 뽑아내서 리스트에서 제거한다.
a = [1, 2, 3, 4, 5]
print(a.pop())  # >> 5
print(a)  # >> [1, 2, 3, 4]
print(a.pop())  # >> 4
print(a)  # >> [1, 2 3]

# 한편, 마지막이 아닌 특정 요소를 제거하고 싶을 때에는 pop() 메소드에 제거하고자 하는 요소의 인덱스를 입력한다.
a = [1, 2, 3, 4, 5]
print(a.pop(3))  # >> 4번째 요소 제거 (4)
print(a)  # >> [1, 2, 3, 5]

# index() /리스트 내에서 매개변수로 입력한 데이터와 일치하는 첫 번째 요소의 첨자를 알려준다.
# 찾고자 하는 데이터와 일치하는 요소가 없으면 오류를 일으킨다.
a = ['abc', 'def', 'ghi']
print(a.index('def'))  # >> 1
# print(a.index('jkl'))  # >> ValueError: 'jkl' is not in list

# count() /매개변수로 입력한 데이터와 일치하는 요소가 몇 개 있는지 센다.
a = [1, 100, 2, 100, 3, 100, 4, 150, 5, 100]
print(a.count(100))  # >> 4
print(a.count(150))  # >> 1
print(a.count(400))  # >> 0

# sort() /리스트 내의 요소를 정렬한다. 매개변수로 reverse = True를 입력하면 내림차순, 아무것도 입력하지 않으면 오름차순으로 정렬한다.
a = [6, 1, 4, 7, 5, 3, 2]
a.sort()
print(a)  # >> [1, 2, 3, 4, 5, 6, 7] (오름차순)
# reverse = True와 같이 이름을 명시하여 사용하는 매개변수를 일컬어 키워드 매개변수라고 한다.
a.sort(reverse=True)
print(a)  # >> [7, 6, 5, 4, 3, 2, 1] (내림차순)

# reverse() /리스트 내 요소의 순서를 반대로 뒤집는다.
a = [4, 9, 2, 6, 8, 7]
a.reverse()
print(a)  # >> [7, 8, 6, 2, 9, 4]
b = ['오', '늘', '저', '녁', '메', '뉴', '는', '쌈', '밥']
b.reverse()
print(b)  # >> ['밥', '쌈', '는', '뉴', '메', '녁', '저', '늘', '오']