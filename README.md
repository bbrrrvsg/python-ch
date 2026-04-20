[ 문법정리 ]
1. 타입 : string, number , boolean
2. 문자열 표현 : " " , ' ' , """ """
3. 이스케이프문자 : \\ \" \' \n \t 
4. 문자열길이 : len( 자료 )
5. 인덱싱 : 문자열[ 인덱스 ]
6. 슬라이싱 : 문자열[ 인덱스 : 인덱스 ]
7. 숫자 종류 : int, float 
8. 사칙연산자 : + * - / // % **
9. 복합대입연산자 : += *= -= /= %= **=
10. 출력 : print( )
11. 입력 : input( )
12. 타입변환 : int( ) , float( ) , str( )

# Python 치트시트 — 개발 참고용

---

## 변수 & 타입

```python
x = 10                          # int
y = 3.14                        # float
s = "hello"                     # str
b = True                        # bool
n = None                        # 없음

a, b = 1, 2                    # 동시 할당
a, b = b, a                    # swap

int("123")                      # str → int
str(123)                        # int → str
float("3.14")                   # str → float
type(x)                         # 타입 확인
isinstance(x, int)              # 타입 체크
```

## 문자열

```python
s = "Hello, World!"

s[0]            # 'H'
s[-1]           # '!'
s[0:5]          # 'Hello'
s[::-1]         # 뒤집기

s.upper()       # 대문자
s.lower()       # 소문자
s.strip()       # 양쪽 공백 제거
s.split(",")    # ['Hello', ' World!']
",".join(lst)   # 리스트 → 문자열
s.replace("a", "b")
s.find("World")        # 9 (없으면 -1)
s.startswith("He")     # True
s.count("l")           # 3

# f-string
f"이름: {name}, 점수: {score:.2f}"
f"{value:>10}"          # 오른쪽 정렬
f"{num:,}"              # 1,000,000
f"{x = }"               # 디버깅용 (3.8+)
```

## 리스트

```python
lst = [1, 2, 3]

lst[0]                  # 인덱싱
lst[1:3]                # 슬라이싱
lst[-1]                 # 마지막 요소

lst.append(4)           # 끝에 추가
lst.insert(0, 99)       # 위치에 삽입
lst.extend([5, 6])      # 리스트 합치기
lst.pop()               # 마지막 제거 후 반환
lst.pop(0)              # 인덱스 제거 후 반환
lst.remove(3)           # 값으로 제거
del lst[0]              # 인덱스로 삭제

lst.sort()              # 정렬 (원본 변경)
lst.sort(reverse=True)  # 내림차순
sorted(lst)             # 정렬 (새 리스트)
lst.reverse()           # 뒤집기
lst.index(2)            # 값의 위치
lst.count(1)            # 값의 개수
len(lst)                # 길이

# 언패킹
a, b, c = [1, 2, 3]
first, *rest = [1, 2, 3, 4]    # first=1, rest=[2,3,4]

# 깊은 복사
import copy
deep = copy.deepcopy(lst)
```

## 튜플

```python
t = (1, 2, 3)
t = 1, 2, 3            # 괄호 생략 가능
single = (1,)           # 요소 1개면 콤마 필수
x, y, z = t             # 언패킹
# 불변! 수정 불가
```

## 딕셔너리

```python
d = {"name": "홍길동", "age": 25}

d["name"]                   # 접근 (없으면 KeyError)
d.get("name")               # 접근 (없으면 None)
d.get("phone", "없음")      # 기본값 지정
d["email"] = "a@b.com"      # 추가/수정
d.update({"age": 26})       # 여러 개 수정

d.keys()                    # 키 목록
d.values()                  # 값 목록
d.items()                   # (키, 값) 쌍

d.pop("age")                # 키 삭제 후 값 반환
del d["name"]               # 삭제
"name" in d                 # 키 존재 확인

d.setdefault("city", "서울")  # 없으면 추가, 있으면 기존값

# 순회
for k, v in d.items():
    print(k, v)

# 병합 (3.9+)
merged = d1 | d2
```

## 세트

```python
s = {1, 2, 3}
s = set([1, 1, 2, 2, 3])   # {1, 2, 3} 중복 제거

s.add(4)
s.remove(1)         # 없으면 KeyError
s.discard(999)      # 없어도 OK

s1 & s2              # 교집합
s1 | s2              # 합집합
s1 - s2              # 차집합

# 중복 제거 활용
unique = list(set(my_list))
```

## 조건문

```python
if x > 0:
    print("양수")
elif x == 0:
    print("영")
else:
    print("음수")

# 삼항
result = "짝수" if x % 2 == 0 else "홀수"

# match-case (3.10+)
match command:
    case "start":
        pass
    case "stop" | "quit":
        pass
    case _:
        pass
```

## 반복문

```python
# for
for x in [1, 2, 3]:
    print(x)

for i in range(5):           # 0~4
for i in range(1, 6):        # 1~5
for i in range(0, 10, 2):    # 0,2,4,6,8

# enumerate — 인덱스 + 값
for i, val in enumerate(lst):
    print(i, val)

for i, val in enumerate(lst, start=1):
    print(i, val)

# zip — 여러 리스트 동시 순회
for a, b in zip(list1, list2):
    print(a, b)

# while
while 조건:
    pass

# break / continue
for x in range(10):
    if x == 3: continue   # 건너뛰기
    if x == 7: break      # 탈출

# for-else (break 안 걸리면 else 실행)
for x in lst:
    if x == target: break
else:
    print("못 찾음")
```

## 컴프리헨션

```python
# 리스트
[x**2 for x in range(10)]
[x for x in lst if x > 0]
["짝" if x%2==0 else "홀" for x in range(5)]

# 딕셔너리
{k: v for k, v in items}
{x: x**2 for x in range(5)}

# 세트
{len(w) for w in words}

# 제너레이터 (메모리 절약)
gen = (x**2 for x in range(1000000))
```

## 함수

```python
def add(a, b):
    return a + b

# 기본값
def greet(name, msg="안녕"):
    return f"{msg}, {name}"

# *args, **kwargs
def func(*args, **kwargs):
    print(args)      # 튜플
    print(kwargs)    # 딕셔너리

# 여러 값 반환
def get_both():
    return min_val, max_val

a, b = get_both()

# 람다
square = lambda x: x**2
add = lambda a, b: a + b
```

## map / filter / sorted

```python
list(map(int, ["1","2","3"]))           # [1, 2, 3]
list(map(lambda x: x*2, [1,2,3]))      # [2, 4, 6]
list(filter(lambda x: x>0, [-1,0,1]))  # [1]

sorted(lst, key=lambda x: x["age"])
sorted(lst, key=len, reverse=True)

# 여러 기준 정렬
sorted(data, key=lambda x: (x[0], -x[1]))
```

## 클래스

```python
class Dog:
    species = "개"              # 클래스 변수

    def __init__(self, name):
        self.name = name        # 인스턴스 변수

    def bark(self):
        return f"{self.name} 멍!"

    def __str__(self):          # print() 시 호출
        return f"Dog({self.name})"

# 상속
class Puppy(Dog):
    def __init__(self, name, toy):
        super().__init__(name)
        self.toy = toy

# property
class User:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, val):
        if val < 0: raise ValueError
        self._age = val

# dataclass (3.7+)
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float
```

## 예외처리

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"에러: {e}")
except (ValueError, TypeError):
    print("값/타입 에러")
except Exception as e:
    print(f"기타: {e}")
else:
    print("에러 없음")
finally:
    print("항상 실행")

# 예외 발생
raise ValueError("잘못된 값")
```

## 파일

```python
# 읽기
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()          # 전체
    lines = f.readlines()       # 줄 단위 리스트
    for line in f:              # 한 줄씩 (메모리 효율)
        print(line.strip())

# 쓰기
with open("file.txt", "w", encoding="utf-8") as f:
    f.write("내용\n")

# JSON
import json
json.dump(data, f, ensure_ascii=False, indent=2)   # 파일에 쓰기
data = json.load(f)                                  # 파일에서 읽기
json.dumps(data)                                     # dict → str
json.loads(json_str)                                 # str → dict
```

## 자주 쓰는 내장함수

```python
len(x)              # 길이
abs(-5)             # 절대값
max(1,2,3)          # 최대
min(1,2,3)          # 최소
sum([1,2,3])        # 합
round(3.14, 1)      # 반올림
any([F, T, F])      # 하나라도 True?
all([T, T, F])      # 전부 True?
zip(a, b)           # 묶기
enumerate(lst)      # 인덱스+값
map(func, lst)      # 각 요소에 적용
filter(func, lst)   # 조건 필터
sorted(lst)         # 정렬
reversed(lst)       # 뒤집기
isinstance(x, int)  # 타입 체크
dir(obj)            # 메서드 목록
```

## collections

```python
from collections import Counter, defaultdict, deque

Counter("aabbcc")               # {'a':2, 'b':2, 'c':2}
Counter(lst).most_common(3)     # 상위 3개

dd = defaultdict(list)
dd["key"].append("val")         # 키 없어도 자동 생성

dq = deque([1,2,3])
dq.appendleft(0)                # 왼쪽 추가
dq.popleft()                    # 왼쪽 제거
```

## 이터레이터 / 제너레이터

```python
# 이터레이터 프로토콜
class Counter:
    def __init__(self, end):
        self.current = 0
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1

# 제너레이터 (간편한 이터레이터)
def count_up(n):
    i = 0
    while i < n:
        yield i
        i += 1

gen = count_up(5)
next(gen)           # 0
next(gen)           # 1
list(count_up(5))   # [0, 1, 2, 3, 4]
```

## 데코레이터

```python
from functools import wraps

def my_deco(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("before")
        result = func(*args, **kwargs)
        print("after")
        return result
    return wrapper

@my_deco
def hello():
    print("hello!")
```

## 타입 힌트

```python
def greet(name: str) -> str:
    return f"안녕, {name}"

def process(items: list[int]) -> dict[str, int]:
    pass

# Optional (None 가능)
from typing import Optional
def find(id: int) -> Optional[str]:
    return None
```

## 정규표현식

```python
import re

re.search(r"\d+", text)        # 첫 번째 매칭
re.findall(r"\d+", text)       # 모든 매칭 리스트
re.sub(r"\d", "*", text)       # 치환
re.split(r"[,;]", text)        # 분리

# \d 숫자  \w 워드  \s 공백  . 아무거나
# + 1회이상  * 0회이상  ? 0or1  {n} n회
```