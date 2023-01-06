# 자료형 비교
| |리스트|튜플|세트|딕셔너리|
|:---:|:---:|:---:|:---:|:---:|
|**선언**|list = []|tuple = ()|set = {}|dictionary = {key:value}|
|**순서보장**|O|O|X|O(v3.7↑)|
|**중복허용**|O|O|X|X(key)|
|**접근**|list[index]|tuple(index)|X|dictionary[key], dictionary.get(key)|
|**수정**|O|X|X|O(value)|
|**추가**|append(), insert(), extend()|X|add(), update()|dictionary[key] = value, update()|
|**삭제**|remove(), pop(), clear()|X|remove(), discard(), pop(), clear()|pop(), popitem(), clear()|


##
```
01. 여러 값들을 순서대로 관리해야 한다면?
> list

02. 값이 바뀔 일이 없거나, 바뀌면 안된다고하면?
> tuple

03. 특정 값의 존재 여부가 있는지 없는지 중요하고, 중복을 허용하지 않는 데이터들인 경우에는?
>set

04. key를 통해 효율적으로 데이터를 관리하고 싶다면?
> dictionary
```
