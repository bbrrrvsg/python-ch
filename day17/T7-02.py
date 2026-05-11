import requests 
from bs4 import BeautifulSoup 
import time 
import pandas as pd   


# [1] 주소 확인 :https://www.yes24.com/product/category/bestseller?categoryNumber=001
# url = 'https://www.yes24.com/product/category/bestseller?categoryNumber=001'

book_List = []
# [2] 주소 매개변수 분석 : , categoryNumber , 
# 1~3 페이지 크롤링 예 
for page in range(1,4):
    url = f'https://www.yes24.com/product/category/bestseller?PageNumber={page}'
    
    # [3] url 요청
    response = requests.get(url)
    
    # [4] 요청한 url 의 성공했을때 HTML 파싱
    soup = BeautifulSoup(response.text, 'html.parser')
    # [5] 가져올 식별자 , soup.selet() : 여러개 , soup.select_one() : 한개
    # 책여러개 : #yseBsetList 여러개 책정보 , li(책하나)
    books = soup.select('#yesBestList > li') # 책 여러개 
    
    # 책하나당 : (.gd_name 제목 , .yes_b 가격 , .info_auth 저자)
    for book in books:
        # strip() : 문자열 양쪽 공백 제거 , get_text() : 요소의 텍스트만 추출
        title = book.select_one('.gd_name').get_text().strip() # 양쪽 공백 제거
        price = book.select_one('.yes_b').get_text().strip() # 양쪽 공백 제거
        author = book.select_one('.info_auth').get_text().strip().replace('\n', '') # 양쪽 공백 제거 + 줄바꿈 제거
        print(title, price, author)
        
        # [6] 리스트에 딕셔너리 포함하기 
        book_List.append({"제목": title, "가격": price, "저자": author})
    
    # [7] import time , time.sleep(초) , 지정한 초만큼 코드(스레드) 가 대기 상태 , 즉] 여러개 크롤링 할때 서버 과부하 방지  
    time.sleep(2) # 2초 대기 -> 서버에 부담 줄이기 위해
    
# [8] 판다스에 넣어주기 
print(book_List)
df = pd.DataFrame(book_List)
print(df)
