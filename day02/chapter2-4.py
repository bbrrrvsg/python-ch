
# 문자열의 format() 함수 , System.out.println("%s" , 10)
String_a = "{}".format(10)
print(String_a , type(String_a))

format_a = "{}만원".format(5000)
print(format_a)
format_b = "{} {} {}".format(1,"유재석",True) # {} 개수 와 자료개수 일치해야한다. 
print(format_b)

# 특정 칸에 출력하기 , {:자릿수d}
output_a = "{:5d}".format(52)  # 52   { } 안에서 공백 주의 
print(output_a)
output_b = "{:05d}".format(52) # 00052 
print(output_b)

# 기호 붙여 출력하기 , {:+d}
output_c = "{:+d}".format(52)
print(output_c)
output_d = "{:+d}".format(-52)
print(output_d)

# 부동소수점 출력하기 
output_e = "{:15f}".format(52.273)
print(output_e)
output_f = "{:+015f}".format(52.273) # + 기호 , 0으로채움 , 15자리수 , f 실수 
print(output_f)
output_g = "{:15.3f}".format(52.2737) # 소수자릿수f ,만약에 잘린 소수점에서 반올림 된다 
print(output_g)

# 의미없는 소수점 제거하기 
output_h = "{:g}".format(52.0)
print(output_h)

# {:g}	52.2730 ->	52.273	끝에 붙은 의미 없는 0만 제거

# 대소문자 바꾸기 
a = "Hello Python"
print(a.upper()) # 대문자 
print(a.lower()) # 소문자 

# 공백 제거하기  ,strip() 양쪽 공백 제거 , lstrip() , rstrip()  
b = "                            ㅎㅇ          "  
print(b.strip())


# 문자열 찾기 
out_a= "안녕안녕하세요".find("안녕")
print(out_a) # 0 번 인덱스에 안녕 존재 한다 

out_b = "안녕안녕하세요".rfind("안녕")
print(out_b) # 2번인덱스 에 "안녕" 존재한다 

print("안녕" in "안녕하세요") # True 
print("잘자" in "안녕하세요") # False

# 문자열 자르기 
out_c = "10 20 30 40 50".split(" ")
print(out_c) # 배열 

