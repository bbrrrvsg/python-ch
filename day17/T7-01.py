
# 웹크롤링 : 웹페이지 존재하는 데이터들을 수집하는 기술 
# 기초지식 : HTML/CSS (식별자) 필요 
# 파이썬 크롤링 라이브러리 : request , BeautifulSoup 정적 , Selenium , Playwright 동적(js/대기) 등 
# 크롤링(로봇) 허용 여부 확인 : 도메인/robots.txt 
# 예] https://www.jobkorea.co.kr/robots.txt ,  Disallow 불가능 , Allow 가능 
 
# [1] HTML/CSS 식별자( 마크업 , #id , .class , 자손선택자 띄어쓰기 , 자식선택자 >) 찾기  
# 브라우져 개발자 도구[f12] -> 왼쪽상단에 마우스 아이콘 (CTRL + SHIFT + C)클릭 -> 크롤링 요소 선택 -> 확인 

# [2] 파이썬 크롤링 
# 네이버검색어 -> 안양날씨 -> 현재 날씨 크롤링 
# 1. 주소               :https://search.naver.com/search.naver?where=nexearch&query=안양날씨
# 쿼리스트링 : URL?변수명=값&변수명=값
# url에서는 한글 불가능 , 인코딩 필요하다 
# 2. 크롤링 선택자       : .temperature_text


# [3] 정적 라이브 러리 
import requests 
from bs4 import BeautifulSoup 

# (1) requests.get(url)
response = requests.get('https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&q=안양날씨')
print(response) # <Response [200]> : 200 성공 , 404 페이지 없음 , 500 서버 오류

# (2) 요청된(200)된 url 에서 HTML 형식으로 파싱하기 : BeautifulSoup(response.text, 'html.parser')
soup = BeautifulSoup(response.text, 'html.parser') # HTML문서 파싱 -> 객체화
print(soup) # <html> ~ </html>

# (3) 가져온 HTML 에서 특정한 요솟 (식별자)만 가져오기 
txt_temp = soup.select_one('.txt_temp')
print(txt_temp) 

# (4) 가져온 요소 에서 텍스트만 추출 , <마크업> *텍스트* </마크업> , 요소변수.get_text()
print(txt_temp.get_text()) # 18.2

