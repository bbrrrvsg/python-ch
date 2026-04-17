
# 딕셔너리 란? 키를 기반으로 값을 저장하는 것 
# vs js(json) vs java(map/dto)

#[1]선언 
dict_a = {"name" : "어벤져스" , "type":"히어로"}

#[2]호출 
print(dict_a)
# print(dict_a.name) # js는 가능하지만 오류 발생 
print(dict_a["name"])
print(dict_a.get("name")) # java map 처럼 사용가능 

# print(dict_a["origin"]) # 없는 키 이면 오류 발생 

#[3] 딕셔너리 값 추가 하기 
dict_a["price"]=1000
print(dict_a)

dict_a["price"] = 2000 # 만약에 존재하는 key 이면 value 수정 
print(dict_a) # key는 중복 없음 

# 딕셔너리 키/값 제거하기 
del dict_a["price"]
print(dict_a)

# 반복문과 딕셔너리 관계 
# for 키 in 딕셔너리명 : 

for 키 in dict_a:
    print(키, ":" , dict_a[키])
    
# 확인 문제 

#(1)
dict_a['name'] = "구름"
del dict_a['name']

#(2)
pets = ['name' : "rrr" , "age": 5]
for key in pets:
    print(key['name'] , key['age'],'살')
    

#(3)

