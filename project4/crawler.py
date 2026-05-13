import requests
from bs4 import BeautifulSoup 
import time 
import pandas as pd 

# https://www.yes24.com/product/category/bestseller?categoryNumber=001&pageNumber=1&pageSize=120



book_list = []

for page in range(1,10):
    url = f"https://www.yes24.com/product/category/bestseller?categoryNumber=001&pageNumber={page}&pageSize=120"
    
    response = requests.get(url)
    # print(response.text)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    books = soup.select('#yesBestList > li')
    
    # .gd_name = 책 제목 , .yes_b = 책 가격 , .saleNum = 판매지수(span임) , .authPub.info_date = 출판년월 
    
    for book in books: 
        제목 = book.select_one('.gd_name').get_text().strip()
        가격 = book.select_one('.yes_b').get_text().strip()
        판매지수 = book.select_one('.saleNum').get_text().strip()
        출판년월 = book.select_one('.authPub.info_date').get_text().strip()
        
        book_list.append({
            '제목': 제목,
            '가격': 가격,
            '판매지수': 판매지수,
            '출판년월': 출판년월
        })
    time.sleep(2) # 2초 대기
        
# print(book_list)
# print(len(book_list))
df =pd.DataFrame(book_list)
df.to_csv('yes24_bestseller.csv', index=False, encoding='utf-8-sig')
