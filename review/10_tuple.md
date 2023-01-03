# 튜플 1 _내장 자료형
● **리스트와 튜플**의 차이점
* **리스트** : **대괄호 속에 값을 넣고 콤마로 구분**한다.
* **튜플** : **소괄호 속에 값을 넣고 콤마로 구분**한다.
###
● **튜플** = (값1, 값2, ...) #리스트와 달리 한 번 만들면 수정이 불가능하다.
**읽기 전용 리스트**라고 생각해도 됨.
```
my_tuple = ('오예스', '몽쉘') #초코파이를 추가하고 싶어도 못함.

> my_tuple.append('초코파이') 불가능
> my_tuple.remove('오예스')   불가능
```
```
my_tuple = ('오예스', '몽쉘', '초코파이')
my_tuple = ('오예스', '몽쉘', '초코파이', '초코파이') #중복 허용
my_tuple = (1, 2, 3.14, True, False, '아무거나') #뭐든 다 넣을 수 있다.
```
##
**01. 튜플 인덱스**
```
* my_tuple = ('오예스', '몽쉘', '초코파이') #순서보장
인덱스에 해당하는 값에 따라 원하는 위치의 값에 접근할 수 있다.

print(my_tuple[0])
> 오예스
```
##
**02. 튜플 슬라이싱**
```
* my_tuple = ('오예스', '몽쉘', '초코파이')
슬라이싱을 통해 원하는 만큼만 출력도 가능하다.

print(my_tuple[0:2])
> '오예스', '몽쉘'
```
##
**03. 튜플 in**
```
* my_tuple = ('오예스', '몽쉘', '초코파이')
포함 여부도 in 키워드를 통해 확인 가능하다.

print('몽쉘' in my_tuple)
> True
```
##
**04. 튜플 len**
```
* my_tuple = ('오예스', '몽쉘', '초코파이')
길이 확인 또한 가능하다.

print(len(my_tuple))
> 3
```
**05. 그 외 튜플 메소드**
|메소드|의미|
|:---:|:---:|
|**count()**|**어떤 값이 몇 개** 있는지|
|**index()**|**어떤 값이 어디에** 있는지|

# 튜플 2 _내장 자료형
**01. 패킹**
```
* my_tuple = ('오예스', '몽쉘', '초코파이')
> '오예스', '몽쉘', '초코파이'의 값을 my_tuple에 넣는다는 의미이다. 
```
##
**02. 언패킹**
```
* (pie1, pie2, pie3) = my_tuple
> my_tuple에 있는 내용들을 하나씩 꺼내서 pie1, pie2, pie3 변수에 각각 저장한다.
  패킹과는 반대의 개념이다.

ex)
pie1 = '오예스'
pie2 = '몽쉘'
pie3 = '초코파이'
```
##
**03. 언패킹(*)**
```
* numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
  (one, two, *others) = numbers
    1    2     [3, 4, 5, 6, 7, 8, 9, 10] #리스트

언패킹에는 별을 쓸 수 있는데, 위처럼 별을 적음으로써 numbers중에서 
첫 번째 값인 1은 one변수, 2는 two 변수에 넣고 나머지는 모두 others에 집어넣으라는 의미가 된다.

이때 others는 여러 개의 값을 가지지만 튜플이 아닌 '리스트' 형태로 된다.
```
```
필요에 따라 별의 위치를 바꿔 사용할 수 있다.

ex)
* numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
  (*others, nine, ten) = numbers
    [1~8]     9    10


* numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
  (one, *others, ten) = numbers
    1    [2~9]    10
```