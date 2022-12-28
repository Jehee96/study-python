# 문자열 메소드 1
● **메소드(Method)** 란, 클래스 내에 정의된 어떤 동작, **기능**을 하는 코드들의 묶음이다.
* **문자열 메소드**
**문자열.메소드이름(...)** #괄호속에 어떤 내용이 들어갈 수 있다.
```
ex)
letter = 'how are YOU?'

* lower() = 모든 내용을 소문자로 바꾼다.
print(letter.lower())
> how are you?

* upper() = 모든 내용을 대문자로 바꾼다.
print(letter.upper())
> HOW ARE YOU?

* capitalize() = 첫 글자만 대문자로 바꾼다.
print(letter.capitalize())
> How are you?

* title() = 각 단어들의 첫 글자만 대문자로 바꾼다.
print(letter.title())
> How Are You?

* swapcase() = 대소문자를 뒤바꾼다.
print(letter.swapcase())
> HOW ARE you?

* split() = 띄어쓰기를 기준으로 나눠진 결과를 리스트 형태로 반환한다.
print(letter.split())
> ['how', 'are', 'YOU?']

* count() = 글자가 몇 번 쓰였는지 알려준다.
print(count('how'))
> 1
```
# 문자열 메소드 2
```
ex)
s = '나도고등학교'

* startswith() = 문자열이 어떤 문자로 시작하는지, '나도'로 시작하는지 확인한다.
print(s.startswith('나도'))
> True

* endswith() = 어떤 값으로 끝나는지 확인한다.
print(s.endswith('초등학교'))
> False

ex_02)
s = '...나도고등학교...'

* strip() = 앞뒤로 불필요한 부분을 제거해준다.
            괄호 속에 아무것도 넣지 않으면 문자열 앞뒤로 불필요한 공백이 제거된다.
print(s.strip('.'))
> 나도고등학교

ex)
s = '나도고등학교'

* replace() = 찾으려는 문자와 바꾸려는 문자를 입력하면 바꾸려는 문자로 바뀐다.
print(s.replace('고등학교', '고교'))
> 나도고교

* find() = 특정 글자를 인덱스 기준으로 어느 위치에 있는지 찾아준다.
print(s.find('학교'))
> 4

* center() = 문자열을 다른 문자열들 사이에 가운데로 집어넣어준다.
             문자열 길이 지정, 하이픈을 넣으면 나도고등학교를 문자열 앞뒤로 하이픈으로 감싸진 10글자의 문장이 만들어진다.
print(s.center(10, '-'))
> --나도고등학교--
```
