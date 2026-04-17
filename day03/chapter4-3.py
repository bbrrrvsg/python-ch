list = [1,2,3,4,5,6]
# 범위 : range 
#[1] 숫자 1개만 넣는 경우 , 0 부터 n-1 까지 리스트로 반환 
print(list(range(1)))

#[2] 숫자 2개 넣는 경우 , s부터 n-1까지 리스트로 반환 
print(list(0,5))

#[3] 숫자 3개 넣는 경우 , s부터 n-1까지 t만큼 증가 
print(list(0,10,2))

# 반복문 과 범위 활용 
# for 반복변수 in range() 

# 1부터 10까지 
for i in range(1,11):
    print(i)
    
# 1부터 10까지 2씩증가 홀수만 출력     
for i in range(1,11,2):
    print(i)

# 리스트와 범위 조합 
array = [273,24,103,52]
for index in range(len(array)):
    print(array[index])


# 역순 
for i in range(4,0-1,-1):
    print(i) # 4부터 0까지 1씩 감소 
    
for i in reversed(range(5)):
    print(i)