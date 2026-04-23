
# 함수 : 

def 함수명():
    print("안녕하세여.")
    print("안녕하세여.")
    print("안녕하세여.")
    
함수명()

# 매개변수 : 함수 호출/사용할 떄 인자값 저장하는 변수 
def func(value , n):
    for i in range(n):
        print(value)
        
func("안녕하세요" , 5)


# 가변 매개변수 : 매개변수의 개수가 변할 수 있다. 
def func2(n,*values) :           # 매개변수에 * 가변매개변수 사용시 [리스트] 타입 받는다 
    for i in range(n):
        for value in values:     # values = ["안녕하세요" , "즐거운" , "파이썬 프로그래밍"]
            print(value)
        print()

func2(3, "안녕하세요" , "즐거운" , "파이썬 프로그래밍")

# 기본 매개벼수 : 만약에 함수/사용 호출할때 인자값이 없으면 기본값 대입 
def func3( value , n=2):
    for i in range(n):
        print(value)
        
func3("안녕하세요")

# 키워드 매개변수 : 매개변수 이름을 직접 지정하여 매개변수에 대입하는 방법 
def func4(*values , n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()

func4("안녕하세요" , "즐거운" , "파이썬 프로그래밍",3) # n매개변수에 3대입 안된다 
func4("안녕하세요" , "즐거운" , "파이썬 프로그래밍",n=3) # 직접 매개변수명 작성하여 대입하면 된다. 

# 리턴 ? 함수 종료시 반환 되는 키워드 
# 반환값 없는 리턴 
def func6():
    return
print(func6())

# 반환값이 있는 리턴 
def func7():
    return 100
print(func7())


