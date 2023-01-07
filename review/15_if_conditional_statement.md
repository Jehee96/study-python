# if 조건문 1
● if는 만약 ~라면 이라는 조건에 따라서 분기를 태울 수 있다.
* 조건이 참일때만(**True**)이 문장을 수행하도록 할 수 있다.
* 조건이 거짓(**False**) 이면 이 문장이라는 부분은 실행하지 않는다.

* **if** = 만약 ~ 라면 if 내의 문장들이, 그렇지 않다면 **else** 내의 문장들이 실행된다.
##
**01. if**
```
* 코드로 나타내면 이 형태로 쓸 수 있다.

if 조건:                       
   이 문장                      if  ─── ┐
다음 문장              True      ↓      │ 
                             이 문장    │  False
                                ↓       │
                            다음 문장 ←─┘

01. if 띄우고 어떤 조건을 적고 끝에 콜론(:)을 적어준다.

02. 그리고 다음 줄에는 이 조건이 참일 때 실행할 문장을 적는다.
    (반드시 앞에 들여쓰기를 해줘야 한다. space 4번 or tab 1번)
```
``` 
ex)
today = '일요일'
if today == '일요일':
   print('게임 한 판')
print('공부시작')

> 게임 한 판
> 공부 시작

today 수가 일요일이면 이 조건은 참이므로 게임을 먼저 한 판 하고 나서 공부를 시작하게 된다.

ex_02)
today = '화요일'
if today == '일요일':
   print('게임 한 판')
print('공부시작')

> 공부 시작

그런데 오늘이 일요일이 아니라면 if 조건이 거짓이므로 바로 공부를 시작하게 된다.
```
##
**02. if True, False**
```
* 조건이 참이면 이 문장을, 거짓이면 저 문장을 수행하는 방법도 있다.
  조건에 따라 둘 중 하나만 선택하게 된다.

if 조건:
   이 문장                       if    ───── ┐
else:                  True      ↓           ↓    False
   저 문장                     이 문장    저 문장
다음 문장                        ↓           │
                             다음 문장  ←────┘

01. if 조건문 아래에다가 else를 적고 콜론을 적는다.

02. 그 밑에 저 문장 부분 앞에 들여쓰기를 하고 나서 적어준다.

03. 이렇게 하면 if 조건이 만족하면 '이 문장'을, 그렇지 않으면 '저 문장'을 수행하고 나서 다음 문장으로 가게 된다.
```
```
ex)
today = '일요일'
if today == '일요일':
   print('게임 한 판')
else:
  #print('폰 5분만')
print('공부 시작')

> 게임 한 판
> 공부 시작

오늘이 일요일이면 게임 한 판을 하고 공부를 시작하게 된다.
(이 때 else 부분은 실행하지 않게 된다.)

ex_02)
today = '화요일'
if today == '일요일':
  #print('게임 한 판')
else:
  #print('폰 5분만')
print('공부 시작')

> 폰 5분만
> 공부 시작

오늘이 일요일이 아니라면 '게임 한 판' 부분이 무시되고 else 부분이 실행되어서 폰 5분 하고 나서 공부를 시작하게 된다.
```