
# 비교 연산자 : == 같다 !=다르다 >크다 <미만 >=크거나같다 <=작거나같다 
# 문자열 비교 : 가나다/abc 순으로 앞에 있는 것이 작은 값 
print("가방" =="가방") # T 
print("가방" =="하마") # T
print("가방" > "가방") # F  '가' 유니코드로 표현 했을때 와 '하' 유니코드로 표현했을때 

# 범위 논리 , 자바에서 안됨 라이브러리쓰면 가능은 함 
x = 25
print(20<x<30)
print(40<x<60)


# 논리 연산자 : and이면서/그리고 or또는/이거나 not부정/반대 
print(not True) # False 
print(True and True)   # True
print(True and False) # False
print(True or False) # True


