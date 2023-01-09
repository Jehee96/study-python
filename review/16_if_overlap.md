# if 중첩
● 말 그대로 if 문 내에서 또 다른 if 문을 사용하는 경우이다.

```
* 코드로 나타내면 이 형태로 쓸 수 있다.
01. if 문장 다음 줄에 들여쓰기를 하고 나서 이 문장을 적고
02. 이 문장 다음 줄에 중첩된 if문은 이 문장과 동일한 크기 만큼의 들여쓰기를 하고 나서 적는다.
03. 중첩된 if가 참일 때 실행될 저 문장은 또 중첩된 if를 기준으로 들여쓰기를 한 번 더 해야한다.

if 조건1:                           False             
   이 문장                      if  ─── ┐
   if 조건2:              True   ↓      │ 
      저 문장                 이 문장   │
다음 문장                        ↓ False│
                                if  ───→│
                                ↓       │
                            다음 문장 ←─┘

01. 첫 번재 if가 참이라면 일단 이 문장이 실행되고 나서 밑에 있는 두 번째 if를 확인하게 된다.

02. 두 번째 if가 참이면 저 문장이 실행되지만

03. 만약 두 번째 if가 거짓이라면 저 문장은 실행되지 않고 바로 다음 문장으로 넘어가게 된다.
```
##
**01. yellow card**
```
ex)
yellow_card = 0                          foul
foul = True                          True  ↓
                                     yellow_card += 1
if foul:                                   ↓             False
   yellow_card += 1                  yellos_card == 2  ────────┐
   if yellow_card == 2:              True  ↓                   ↓
      print('경고 누적 퇴장')         경고 누적 퇴장     휴.. 조심해야지
   else:
      print('휴..조심해야지')

* 옐로카드를 처음 받는 경우라면 퇴장은 아니지만 앞으로 조심해야 한다.
  그러므로 else를 적고 옐로카드가 두 장이 아닐 때에 대한 처리를 이렇게 해준다.
```
##
```
ex_02)                                                   False
yellow_card = 0                          foul  ────────────────────────────────┐
foul = True                          True  ↓                                   │
                                     yellow_card += 1                          │
if foul:                                   ↓             False                 │
   yellow_card += 1                  yellos_card == 2  ────────┐               │
   if yellow_card == 2:              True  ↓                   ↓               ↓
      print('경고 누적 퇴장')         경고 누적 퇴장     휴.. 조심해야지         주의
   else:
      print('휴..조심해야지')
else:
   print('주의')

* 옐로 카드를 받을 만한 파울이 아닌, 주의 정도만 주는 파울일 때는
  첫 번째 if와 동등한 위치에 else 문을 이용해서 '주의'를 적는다.
```
##
```
ex_03)                                                   False
yellow_card = 0                          foul  ────────────────────────────────┐
foul = True                          True  ↓                                   │
                                     yellow_card += 1                          │
if foul:                                   ↓             False                 │
   yellow_card += 1                  yellos_card == 2  ────────┐               │
   if yellow_card == 2:              True  ↓                   ↓               ↓
      print('경고 누적 퇴장')         경고 누적 퇴장     휴.. 조심해야지         주의
   else:                                   ↓  ←────────────────┴←──────────────┘
      print('휴..조심해야지')            다음 문장
else:
   print('주의')
다음 문장

* 그 이후에는 if문 밖에 있는 다음 문장을 실행하게 될 것이다.
```
