# 리스트 1 _내장 자료형
● **변수와 리스트**의 차이점
* **변수** : **하나**의 값을 저장
* **리스트** : **여러개**의 값을 저장.서로 관련 있는 연속적인 데이터들을 관리한다.

● **리스트** = [값1, 값2, ...] #대괄호 속에 값을 넣고 콤마(,)로 구분 후 선언.
```
my_list = ['오예스', '몽쉘', '초코파이', '초코파이', '초코파이'] #중복가능
your_list = [1, 2, 3.14, True, False, '아무거나'] #뭐든 다 넣을 수 있다.
empty_list = [] #빈 리스트
```
# 리스트 2 _내장 자료형
**01. 리스트 인덱스**
```
* my_list = ['오예스', '몽쉘', '초코파이'] #순서 보장
리스트가 이렇게 선언되었을때 어떤 인덱스에 해당하는 값을 확인하려면
문자열과 같은 방법으로 대괄호 속에 인덱스를 넣어주면 해당 값이 출력된다.
(리스트의 값들은 순서가 보장된다는 특징 때문에 가능하다.)

print(my_list[0])
>오예스
```
##
**02. 리스트 슬라이싱**
```
* my_list = ['오예스', '몽쉘', '초코파이']
print(my_list[0:2])
> ['오예스', '몽쉘']
```
##
**03. 리스트 in**
```
* my_list = ['오예스', '몽쉘', '초코파이']

# 리스트에 포함되어있는지?
print('몽쉘'in my_list)
> True

불리안 형태로 값이 있다면 True, 없다면 False로 출력된다.
```
##
**04. 리스트 len**
```
* my_list = ['오예스', '몽쉘', '초코파이']

# 총 몇 개?
print(len(my_list))
> 3
```
##
**05. 리스트 수정**
```
* my_list = ['오예스', '몽쉘', '초코파이']

# 리스트를 수정하려면?
인덱스를 지정해서 변수 값 변경하는 것처럼 새로운 값을 넣어주면 된다.
my_list[1] = '몽쉘카카오' #값을 수정
print(my_list)
> ['오예스', '몽쉘카카오', '초코파이']
```
##
**06. 리스트 추가(append)**
```
* my_list = ['오예스', '몽쉘', '초코파이']

# 리스트를 추가(수정)하려면?
append()라는 메소드를 이용해서 리스트 맨 뒤에 새로운 값을 추가한다.
my_list.append('빅파이') #값 추가
print(my_list)
> ['오예스', '몽쉘', '초코파이', '빅파이']
```
##
**07. 리스트 삭제(remove)**
```
* my_list = ['오예스', '몽쉘', '초코파이']

# 리스트를 삭제(수정)하려면?
remove() 메소드를 이용해서 괄호 속에 지우려는 값을 입력함으로써 삭제할 수 있다.
my_list.remove('오예스') #값 삭제
print(my_list)
> ['몽쉘', '초코파이']
```
##
**08. 리스트 확장(extend)**
```
* my_list = ['오예스', '몽쉘', '초코파이']
* your_list = ['빅파이', '오뜨']

# 다른 리스트를 더하려면?
my_list.extend(your_list) #리스트 확장
print(my_list)
> ['오예스', '몽쉘', '초코파이', '빅파이', '오뜨']
```
##
**09. 그 외 리스트 메소드**
|메소드|의미|
|:---:|:---:|
|**insert()**|원하는 위치에 **값 추가**|
|**pop()**|원하는 위치(또는 마지막)의 **값 삭제**|
|**clear()**|모든 값 삭제|
|**sort()**|값 순서대로 **정렬**|
|**reverse()**|순서 **뒤집기**|
|**copy()**|리스트 복사|
|**count()**|어떤 값이 **몇 개** 있는지|
|**index()**|어떤 값이 **어디에** 있는지|