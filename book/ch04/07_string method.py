# 4.3.1) 문자열 메소드
# 순서열로부터 물려받은 기능 외에도 문자열은 다양한 기능의 함수를 자체적으로 탑재하고 있다.
# 내장 함수들과는 달리 이런 함수는 문자열 자료형 안에 들어가 있다.
# 이런 특정 자료형이 갖고 있는 함수를 메소드(method)라고 한다.

# 01) startswith() /원본 문자열이 매개변수로 입력한 문자열로 시작되는지를 판단한다. 결과는 True 또는 False로 나온다.
a = 'Hello'
print(a.startswith('He'))
# >>> True
print(a.startswith('lo'))
# >>> False

# 02) endswith() /원본 문자열이 매개변수로 입력한 문자열로 끝나는지를 판단한다. 결과는 True 또는 False로 나온다.
a = 'Hello'
print(a.endswith('He'))
# >>> False
print(a.endswith('lo'))
# >>> True

# 03) find() /원본 문자열 안에 매개변수로 입력한 문자열이 존재하는 위치를 앞에서부터 찾는다. 존재하지 않으면 -1을 결과로 내놓는다.
a = 'Hello'
print(a.find('ll'))
# >>> 2
print(a.find('H'))
# >>> 0
print(a.find('K'))
# >>> -1

# 04) rfind() /원본 문자열 안에 매개변수로 입력한 문자열이 존재하는 위치를 뒤에서부터 찾는다. 존재하지 않으면 -1을 결과로 내놓는다.
a = 'Hello'
print(a.rfind('H'))
# >>> 0
print(a.rfind('lo'))
# >>> 3
print(a.rfind('M'))
# >>> -1

# 05) count()
a = 'Hello'
print(a.count('l'))
# >>> 2
print(a.count('e'))
# >>> 1

# 06) lstrip()
print('        Left Strip'.lstrip())
# >>> Left Strip

# 07) rstrip()
print('Right Strip         '.strip())
# >>> Right Strip

# 08) strip()
print('     Strip       '.strip())
# >>> Strip

# 09) isalpha() /원본 문자열이 숫자와 기호를 제외한 알파벳(영문, 한글 등)으로만 이루어져 있는지를 평가한다.
print('ABCDefgh'.isalpha())
# >>> True
print('123ABC'.isalpha())
# >>> False

# 10) isnumeric() /원본 문자열이 숫자로만 이루어져 있는지를 평가한다.
print('20220924'.isnumeric())
# >>> True
print('20220924 토요일'.isnumeric())
# >>> False

# 11) isalnum() /원본 문자열이 알파벳과 수로만 이루어져 있는지를 평가한다.
print('1234ABC'.isalnum())
# >>> True
print('123456'.isalnum())
# >>> True
print('maratang'.isalnum())
# >>> True

# 12) replace() /원본 문자열에서 찾고자 하는 문자열을 바꾸고자 하는 문자열로 변경한다.
a = 'Hello, World'
b = a.replace('World', 'Korea')
print(b)
# >>> Hello, Korea
a = 'Hello, World, World'
b = a.replace('d, World', 'd !')
print(b)
# >>> Hello, World !

# 13) split() /매개변수로 입력한 문자열을 기준, 원본 문자열을 나눠 '리스트'를 만든다.
a = 'egg, pasta, cream'
b = a.split(',')
print(b)
# >>> ['egg, pasta, cream']

a = 'Im an Englishman in New York'
b = a.split(' ')[4]
print(b.lower())
# >>> new

# 14) upper() /원본 문자열을 모두 대문자로 바꾼 문자열을 내놓는다.
a = 'lower case'
print(a.upper())
# >>> LOWER CASE

# 15) lower() /원본 문자열을 모두 소문자로 바꾼 문자열을 내놓는다.
a = 'UPPER CASE'
print(a.lower())
# >>> upper case

# 16) format() /형식을 갖춘 문자열을 만들때 사용함. 문자열 안에 중괄호{와 }로 다른 데이터가 들어갈 자리를 만들어 두고
# format()함수를 호출할 때 이 자리에 들어갈 데이터를 순서대로 넣어주면 원하는 형식의 문자열을 만들어 낼 수 있다.
c = ['마라탕', '맛있다', '매래댕', '도 맛있따']
a = '{a} 진짜 {b} {c}'
print(a.format(b = c[2], a = c[1], c = c[0]))
# >>> 맛있다 진짜 매래댕 마라탕