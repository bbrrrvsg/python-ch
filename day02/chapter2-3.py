# 변수 : 하나의 자료 저장하는 (메모리) 공간 

pi = 3.141592

print(pi)
print(pi+pi)

# 주의 할점  
# print(pi+"입니다") # 예외가 발생한다. 
print(pi , "입니다") # 연결 

# 타입의 유연성 = 동적 타입 
# 자바 또는 c 언어 , int pi = 3 
# 파이썬 pi =3 

# 복합 대입 연산자 
number = 100 
number += 10 
print(number)

number -=10

number *= 10 

number /=10 

number %=10

number **=10


# 사용자 입력  , 무조건 문자열로 반환
input("인사말을 입력 하세요")

String = input("인사말을 입력 > ")
print(String)
print(type(String))


# 문자열을 숫자로 변환하기  Integer.parseInt() vs parseInt() vs int()
String_a = input("입력 > ")
int_a = int(String_a)
print(type(String_a))

String_b = int(input("입력 > "))
print(type(String_b))

String_c = float(input("입력 > "))
print(type(String_c))



