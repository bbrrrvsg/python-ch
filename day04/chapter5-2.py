# 재귀함수 이란 ? 현재 실행 중인 (자신의) 함수를 다시 호출 하는 것 

# [1] 반복문으로 팩토리얼 구하기 

def func1(n):
    output = 1 
    for i in range(1,n+1):
        output *=1
    
    return output

print("s팩토리얼 : " , func1(5))

# [2] 재귀함수로 팩토리얼 구하기 
def func2( n):
    if n ==0: 
        return 1 
    
    else:
        return n* func2(n-1)
print("5! : ",func2(5))


# [3] 피보나치 수열  1, 1번째 수열 : 1 , 2번째 수열 : 2 , n번째 수열 n-1 수열 + n-2수열 

def func3(n):
    if n ==1 :
        return 1
    if n== 2:
        return 1
    else:
        return func3(n-1)+func3(n-2)
print(func3(4))

# [4] 피보나치 수열2, 메모화 
dictionary = { # 결과를 저장하는 딕셔너리 
    1 : 1,
    2 : 1
}

counter = 0 # 함수 밖에 있는 변수 
def func4(n):
    global counter # 함수 밖에 있는 변수 호출 
    counter+=1
    print(counter)
    
    if n in dictionary:
        return dictionary[n]
    else:
        output = func4()
        
