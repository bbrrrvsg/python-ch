
# 예외처리 : 예외가 발생할 상황을 예측하고 모두 조건문으로 처리하는 것은 매우 힘들다 
# 예외가 발생하면 프로그램이 강제로 종료되지 않게 흐름제어 하기 = 예외처리 
# try: ~except : ~ 

try : 
    number_input_a = int(input('정수입력 : ')) # 7 정상 , a 예외 

except :
    # 만약에 예외가 발생했을 떄 코드  
    print('정수만 입력하세요. ')
    

# pass : 예외처리가 아닌 일단 생략할 경우 

list_input_a = ["52","273","32","스파이","103"]

list_number = []

for item in list_input_a:
    try:
        float(item) # 실수로 변환하는 함수
        list_number.append(item) 
    except:
        pass
print(list_number)

# else  : 예외가 발생하지 않았을떄 실행 코드 

try : 
    number_input_a = int(input('정수 입력 : '))
except :
    print('정수를 입력하세여')
else:
    print(number_input_a)
    

# finally : 무조건 실행할 코드  , try 안에서 return,break
# 해도 무조건 실행 

try : 
    number_input_a = int(input('정수입력 : '))
except :
    print('정수를 입력하세요')
else : 
    print('예외가 발생 하지 않음')
finally :
    print('무조건 실행되는 코드')
    
