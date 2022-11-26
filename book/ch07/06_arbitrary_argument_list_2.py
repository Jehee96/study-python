# 이번에는 반대의 경우로, 일반 매개변수가 가변 매개변수 뒤에 정의되어 있는 함수를 호출할때는
# 일반 매개변수를 키워드 매개변수로 호출해야한다. (일반 매개변수의 이름을 명시해줘야함.)
# 다음은 일반 매개변수를 가변 매개변수 뒤에 정의한 함수를 호출하는 예제 코드이다.
def print_args(*argv, argc):
    for i in range(argc):
        print(argv[i])
        
print_args("argv1", "argv2", "argv3", argc=3)  # argv1
                                               # argv2
                                               # argv3
                                               
# print_args("argv1", "argv2", "argv3", 3)
# Traceback (most recent call last):
#   File "c:/Workstation/JJ/study-python/book/ch07/06_arbitrary_argument_list.py", line 56, in <module>
    # print_args("argv1", "argv2", "argv3", 3)
# TypeError: print_args() missing 1 required keyword-only argument: 'argc'
