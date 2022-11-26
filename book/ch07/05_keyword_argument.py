# 7.3.1) 기본값 매개변수와 키워드 매개변수
# 4장에서 나온 math.log() 함수는 매개변수가 두개이다. math.log(4, 2)를 호출하면 밑을 2로 하는 4의 로그값을 구한다.
# 그런데 두 번째 매개변수를 생략한 채 math.log(10)를 호출하면 자연수 e를 밑으로 하는 10의 로그값을 구해준다.
# 함수가 요구하는 매개변수는 '호출자'가 반드시 입력돼야 한다. 함수를 정의할 때
# "이 매개변수를 입력할지 말지는 호출자 당신의 자유다. 단, 입력하지 않으면 내가 갖고 있는 기본값으로 할당할 것이다."
# 라고 지정할 수 있는 방법이 있다. 기본값 매개변수(Default Argument Value)를 이용하는 방법이다.
# 기본값 매개변수를 정의하고 사용하는 방법은 다음과 같다.
def print_string(text, count=1):
    for i in range(count):
        print(text)

print_string('안녕하세요')     # 안녕하세요

print_string('안녕하세요', 2)  # 안녕하세요
                               # 안녕하세요

# 한편, 호출자가 매개변수의 이름을 일일이 지정해 데이터를 입력하는 것도 가능하다.
# 이것을 키워드 매개변수(Keyword Argument)라고 한다.
def print_personnel(name, position='staff', nationality='Korea'):
    print('name = {0}'.format(name))
    print('position = {0}'.format(position))
    print('nationality = {0}'.format(nationality))

print_personnel(name='박쨈미')                     # position, nationality는 기본값이 사용된다.
# name = 박쨈미
# position = staff
# nationality = Korea

print_personnel(name='박쨈미', nationality='ROK')  # position만이 기본값을 사용한다.
# name = 박쨈미
# position = staff
# nationality = ROK

print_personnel(name='박쨈미', position='인턴')    # nationality만이 기본값을 사용한다.
# name = 박쨈미
# position = 인턴
# nationality = Korea
