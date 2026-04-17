
# 리스트란? 여러 자료들을 모아 하나의 자료로 구성 
#[ , , , ,]
# 인덱스란? 자료가 저장된 순서 , 0번 시작 

list_a = [273,32,"문자열",True]
print(list_a[0])
print(list_a[1:3])

list_a[1] = "변경값"
print(list_a)

print(list_a[-2]) # 문자열

print(list_a[2][1]) # 2 번 인덱스의 첫번쨰 인덱스 문"자"열

list_a[1] =["변경값1","변경값2"] # 리스트 안에 리스트 
print(list_a[1][1]) # 변경값2 


# 리스트 연산 
list_a = [1,2,3]
list_b =[4,5,6]

# [1] + 연결 
print(list_a + list_b)  # [1,2,3,4,5,6]
# [2] * 반복
print(list_a*3)         # [1, 2, 3, 1, 2, 3, 1, 2, 3]
# [3] len 길이 
print(len(list_a))      # 3

# 리스트에 요소 추가 
#[4] 요소 추가하기 
list_a.append(4)
print(list_a)           # [1, 2, 3, 4]


#[5] 중간에 요소 추가하기 
list_a.insert(1,1.5)    # 위치 , 자료 
print(list_a)           # [1, 1.5, 2, 3, 4]

# 리스트 요소 제거 
list_a = [0,1,2,3,4,5,]

#[6] del 리스트명[인덱스]
del list_a[1]
print(list_a)           #[0, 2, 3, 4, 5]

#[7] 리스트명.pop(인덱스)
list_a.pop(2)
print(list_a)
list_a.pop()            # 마지막 인덱스 삭제 
print(list_a)

#[*] 슬라이싱 이란? 인덱스로 구성된 자료들(문자열/리스트)의 요소 선택 가능 
# [시작인덱스 : 끝인덱스 : 단계]
print(list_a)
print(list_a[: : -1]) # [4, 2, 0] 역순 
print(list_a[0::2])   # [0, 4] 0부터 마지막인덱스까지 2칸씩 이동 

#{8} 리스트명.remove(자료) , 해당 자료가 존재하면 삭제 
list_a.remove(2)
print(list_a)

#[9] 리스트명.clear() 
list_a.clear() # 전체삭제
print(list_a)  # []


#[10] .sort() 리스트 정렬 , .sort(reserve = True)
list_a = [52, 222, 190 , 32] 
list_a.sort()       # 오름 차순 
print(list_a)

list_a.sort(reverse=True)   # 내림차순 
print(list_a)


#[11] in , 내부에 있는지 확인 
print(190 in list_a) # True 
print(250 in list_a) # False 
print(190 not in list_a) # True -> False 



# 리스트와 반복문 
# for 반복변수 in 반복할수 있는 자료 
# 코드 