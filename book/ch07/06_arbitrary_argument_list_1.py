# 7.3.2) 가변 매개변수
# str.format() 함수는 매개변수의 수가 유동적이다. 아무것도 입력하지 않아도 되고 10개, 20개를 입력해도 제대로 동작한다.
# 상황에 따라 매개변수의 수가 달라지는 이런 함수는 '가변 매개변수(Arbitrary Argument List)'라는 것을 이용하여 만든다.
# 형식은 다음과 같다.
# def 함수이록(*매개변수):  # 매개변수 앞에 *를 붙이면 해당 매개변수는 '가변'으로 지정된다.
#     코드블록

# merge_string() 함수는 가변 매개변수를 이용해 여러개의 문자열을 입력받아 이어붙이는 기능을 한다.
def merge_string(*text_list):
    result = ''
    for s in text_list:
        result = result + s
    return result

print(merge_string('쨈미가', '내빵을', '먹어버렸다.'))  # '쨈미가내빵을먹어버렸다.'

# 위 예제 코드는 가변 매개변수인 'text_list'를 '순서열'처럼 다루고 있다.
# *를 이용하여 정의된 가변 매개변수는 튜플이다. 따라서 text_list를 다룰 때는 순서열을 다룰 때 사용했던 연산을 모두 사용할 수 있다.
# 가변 매개변수의 종류는 하나 더 있는데, *를 두 개 사용하여(**) 가변 매개변수의 이름 앞에 붙여주면 그 가변 매개변수는 딕셔너리 타입으로 정의된다.
# 다음은 딕셔너리 가변 매개변수를 이용하는 함수의 예제 코드이다.
def print_team(**players):
    for k in players.keys():
        print('{0} = {1}'.format(k, players[k]))
        
print_team(카시야스='GK', 호날두='FW', 알론소='MF', 페페='DF')  # 카시야스 = GK
                                                                # 호날두 = FW
                                                                # 알론소 = MF
                                                                # 페페 = DF
                                                                
# 대개 가변 매개변수만 단독으로 사용하는 경우보다 일반 매개변수와 함께 사용하는 경우가 더 많다.
# 그런데 가변 매개변수와 함께 사용하는 일반 매개변수는 정의 순서에 따라 호출바익이 달라진다.
# 가변 매개변수의 '앞'에 정의되는 일반 매개변수는 키워드 매개변수를 이용할 수 없다.
# 매개변수 명을 명시하지 않고 호출하면 정상적으로 실행되지만 키워드 매개변수로 호출했을 때는 문법 에러가 출력된다.
def print_args(argc, *argv):
    for i in range(argc):
        print(argv[i])
        
print_args(3, "argv1", "argv2", "argv3")  # argv1
                                          # argv2
                                          # argv3
                                          
# print_args(argc=3, "argv1", "argv2", "argv3")
# SyntaxError: positional argument follows keyword argument
