# 연습문제

**01. 다음 중에서 결과가 다른 것을 하나 고르세요.**
> 1) not False
> 2) not 0
> 3) not None
> 4) not 'ABC'
```
답 : 1
```

**02. 다음 중 결과가 True인 것은 무엇입니까?**
> 1) True and False 
> 2) True or not False
> 3) False and not False
```
답 : 2
```

**03. 다음 코드의 실행결과는 무엇입니까?**
> ```
> a = 0
> if a:
>     print("1")
> else:
>     print("2")
```
답 : 2
```

**04. 다음과 같은 결과를 출력하는 프로그램을 for문을 이용하여 작성하세요. 규칙은 첫 번째 줄에 별 하나, 두 번째 줄에 별 둘, 세 번째 줄에 별 셋. 이런 식으로 5개의 별이 찍힐 때까지 반복합니다(힌트 : for문 블록 안에 for문 블록을 넣으세요).**
> ```
> *
> **
> ***
> ****
> *****
```
답 : for i in range(0, 5):
    star = ''
    for j in range(0, i+1):
        star = star + '*'
    print(star)
```

**05. 다음과 같은 결과를 출력하는 프로그램을 for문을 이용해 작성하세요.**
> ```
> *****
> ****
> ***
> **
> *
```
답 : for i in range(5, 0, -1):
    star = ''
    for j in range(0, i):
        star = star + '*'
    print(star)
```

**06. 4번과 5번을 for문 대신 while문으로 바꿔서 작성하세요.**
```
답 : 4번
i = 0
while i < 5:
    star = ''
    j = i + 1
    while j > 0:
        star = star + '*'
        j -= 1
    i += 1
    print(star)

    5번
i = 5
while i > 0:
    star = ''
    j = 0
    while j < i:
        star = star + '*'
        j += 1
    print(star)
    i -= 1
```

**07. 다음과 같이 사용자로부터 입력 받은 횟수만큼 별을 반복 출력하는 프로그램을 작성하세요. 단, 입력받은 수가 0보다 작거나 같을 경우 "0보다 작거나 같은 숫자는 사용할 수 없습니다."라는 메시지를 띄우고 프로그램을 종료합니다.**
> ```
> 반복횟수를 입력하세요 : -10
> 0보다 작거나 같은 수는 입력할 수 없습니다.

> 반복횟수를 입력하세요 : 5

```
> *
> **
> ***
> ****
> *****
```
답 : num = int(input('반복횟수를 입력하세요 : '))

if num <= 0:
    print("0보다 작거나 같은 숫자는 사용할 수 없습니다.")
    exit(0)
    
print(num)

for i in range(0, num):
    star = ''
    for j in range(0, i+1):
        star = star + '*'
    print(star)
```
