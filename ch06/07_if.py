# 6.2.1) if문
# 파이썬에서는 분기문을 if문 한 종류만 제공한다.
# if는 '만약 ~라면'의 뜻을 갖고 있으며, 영어에서 어떤 상황을 가정할 때 사용하는 말이다.
# '만약 입력받은 수 a가 0이라면' 처럼 말이다.

# if 조건:            # if 뒤에 흐름을 가를 조건이 위치하고, 그 뒤에 콜론(:)이 온다.
#     명령 1          # : 뒤에는 들여쓰기로 이루어진 코드블록이 온다. 이 코드블록은 if문의 조건이 'True'일 경우 실행된다.
#     명령 2

# else:               # if문의 조건을 충족하지 않을 때, 조건 평가의 결과가 'False'일 때의 흐름은 'else'로 향한다.
#     명령 3          # else 뒤에도 코드블록이 오므로 콜론(:)이 위치해야 한다.
#     명령 4

# if문의 조건은 '참' 아니면 '거짓'으로 평가될 수 있어야 한다.
# 조건 뒤에 있는 콜론(:)은 해당 조건이 참일 경우에 실행할 코드블록을 위치시키기 위함이다.
# 콜론이 필요한 것은 'else'절에 대해서도 마찬가지이며, else 절로 코드가 흐르는 경우는 if절의 조건이 '거짓'으로 평가되었을 때다.

# 01) ifelse.py (if와 else의 예제 코드)
a = int(input('수를 입력하세요 : '))  # >> input()은 콘솔(도스창)로부터 입력받는 함수이다.
                                      # 입력받은 문자열로 나오기 때문에 int()함수를 이용해 정수 형식으로 변환한다.
if a == 0 :
    print('0은 나눗셈에 이용할 수 없습니다.')
else :
    print('3 /', a, '=', 3/a)

# 02) if.py (if문에서 else절은 필수사항이 아니다. 위의 예제 코드를 다음과 같이 else를 제거한 버전으로 바꿀 수 있다.)
import sys  # >> 파이썬 프로그램을 종료하는 exit() 함수를 사용하기 위해 sys 패키지를 임포트한다.
a = int(input('수를 입력하세요 : '))

if a == 0:  # >> if not a: 와 동일한 코드
    print('0은 나눗셈에 이용할 수 없습니다.')
    sys.exit(0)  # >> a가 0인 경우 경고 메시지를 출력한 뒤 프로그램을 종료시킨다.
                 # 순서도와 기능만 놓고 보면 위의 예제와 같다고 볼 수 있다.
print('3 /', a, '=', 3/a)

# 한 가지 조건만 다룰 때는 if 또는 if~else로 충분하다.
# 하지만 여러 조건을 생각해야 하는 경우는 if와 함께 elif를 사용한다. 'elif'는 'else if'를 줄여 만든 파이썬 키워드이다.

# if 조건1:    # >> 첫 번째 조건을 '항상 if'로 시작한다.
     # 코드블록
     # ...
     
# elif 조건2:  # >> 두 번째 조건부터는 'elif'를 이용한다.
     # 코드블록
     # ...
     
# elif 조건3:
     # 코드블록
     # ...
     
# elif 조건4:
     # 코드블록
     # ...
     
# else:        # >> 마지막의 else는 생략할 수 있다.
     # 코드블록
     # ...
     
# 03) ifelif.py (if와 elif 예제 프로그램)
dow = input('요일(월 ~ 일)을 입력하세요 : ')

if dow == '월':
    print('Monday')
elif dow == '화':
    print('Tuesday')
elif dow == '수':
    print('Wednesday')
elif dow == '목':
    print('Thursday')
elif dow == '금':
    print('Friday')
elif dow == '토':
    print('Saturday')
elif dow == '일':
    print('Sunday')
else:
    print('잘못 입력된 요일입니다.')

# 코드블록은 또 다른 흐름 제어문을 가질 수 있다.
# if문의 코드블록에 또 다른 if문을 넣을 수 있으며, if문 안의 if문도 코드블록이 필요하다.
# 이럴 때에는 안쪽 if문의 코드블록은 바깥 쪽의 코드블록보다 들여쓰기를 한 단계 더 깊이 해줘야 한다.

# 04) ifif.py
a = int(input('수를 입력하세요 : '))

if a > 10:
    if a % 2 == 0:               # if a > 10 : 의 코드블록 
        print('10보다 큰 짝수')  # a > 10이 참인 경우 if a % 2 == 0: 의 코드블록
    else:
        print('10보다 큰 홀수')  # a > 10이 참인 경우 else: 의 코드블록
else:
    if a % 2 == 0:
        print('10 이하의 짝수')
    else:
        print('10 이하의 홀수')

# 여러 조건을 평가할 때 중첩 if문 대신 and 또는 or 연산자를 이용하는 것도 좋은 방법이다.

# 05) ifand.py (and 연산자를 이용하여 중첩 if문을 제거한 버전)
a = int(input('수를 입력하세요 : '))

if a > 10 and a % 2 == 0:
    print('10보다 큰 짝수')
elif a > 10 and a % 2 != 0:
    print('10보다 큰 홀수')
elif a % 2 == 0:
    print('10이하의 짝수')
else:
    print('10이하의 홀수')

# a = int(input('수를 입력하세요 : '))

# if a > 10 and a % 2 == 0:
#     print('10보다 큰 짝수')
# elif a > 10 and a % 2 != 0:
#     print('10보다 큰 홀수')
# elif a % 2 == 0:
#     print('10이하의 짝수')
# else:
#     print('10이하의 홀수')

# 블럭형 응용 1
# output = '10 초과의 '

# if a <= 10:
#     output = '10 이하의 '

# if (a & 1) != 0:
#     output = output + '홀수'
# else:
#     output = output + '짝수'

# print(output)