# 6.3) 반목분
# 반복문은 프로그램의 흐름을 되풀이하는 '루프문(Loop Srarement)'이라고도 한다.

# 6.3.1) while문
# 파이썬에서는 코드의 흐름을 '반복'시킬 수 있는 'while문'과 'for문' 두 가지 방법을 제공한다.

# while문은 다음 형식으로 사용한다.
# while 조건:
   # 코드블록
   
# while 키워드가 먼저 위치하고 그 다음에 조건이 온다. 조건 뒤에는 코드블록을 위치시키기 전에 콜론(:)이 있어야 한다.
# while은 영어로 '~하는 동안'이라는 뜻으로 while 코드를 읽을 때는 '조건이 참인 동안'이라고 해석하면 이해가 쉽다.

# 01) while.py (예제1)
limit = int(input('몇 번 반복할까요? : '))

count = 0
while count < limit:             # >> 이 while문은 'count가 limit보다 작은 동안'은 이어지는 코드블록을 반복 실행한다.
    count = count + 1            # >> count를 1씩 증가시킨다.
    print('{count}회 반복.'.format(count=count))
    
print('반복이 종료되었습니다.')  # >> count < limit이 거짓이면 while문은 반복을 멈춘다. 그리고 이 문장을 실행한다.

# while문이 반복을 계속할지를 판단하는 조건이 항상 True인 경우를 만들면 프로그램의 흐름은 영원히 해당 while문의 코드블록을 반복한다.
# 이것을 무한루프(Infinite Loop)라고 하며, 365일 멈추지 않고 임무를 수행해야 하는 서버나 게임 소프트웨어는 이를 필요로 한다.
# while True:
    # 코드블록

# 02) while_infinite.py (예제2)
while True:
    answer = input('반복을 계속할까요? [예/아니오] : ')
    
    if answer == '예':
        print('반복을 계속합니다.')
    elif answer == '아니오':
        break  # >> break는 반복문의 실행을 취소시키는 기능을 한다.
    else:
        print('정상적인 답변이 아닙니다.')
    