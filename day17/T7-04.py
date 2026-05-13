
# 동적페이지 크롤링 
# - 웹페이지 자료가 대기 상태 / 이벤트가 있는 경우 

# [1] 섳치 
# pip install playwright        # 파이썬 라이브러리 
# playwright install            # 크롤링에 필요한 브라우저 설치

# [2] 라이브러리
import asyncio # 비동기 라이브러리 
from playwright.async_api import async_playwright # 동적웹페이지 크롤링 라이브러리 
import pandas as pd 

# [3] 크롤링 주소 
# url = 'https://search.naver.com/search.naver?where=image&query=짱구'

# tile_item _fe_image_tab_content_tile is_visible
# 박스 : tile_item , 이미지 : _fe_image_tab_content_thumbnail_image , 제목 : info_title


# [4] 동기 웹 크롤링 

async def naverRun(): # 동기화 된 함수 
    # (1) playwright 실행하고 p 변수에 결과 받기 
    async with async_playwright() as p : # 
        # (2) await(대기) 상태 이용한 크롬 실행 , await.chromium.launch()  
        # headless=False : 브라우져가 직접 실행된다. <봇 차단 방지> 
        browser = await p.chromium.launch(headless=False) 
        
        # (3) 실행된 브라우져(chromium) 에서 새로운 페이지에 지정한 URL 대입하여 이동 
        url = 'https://search.naver.com/search.naver?where=image&query=짱구'    # url 
        page = await browser.new_page()                                         # 새로운 페이지 열기 
        await page.goto(url)                                                    # url 이동
        
        # (4) (자료가 표시될떄 까지 기다리기) 대기 상태 만들기 
        # (4-1) 스크롤 내리기 이벤트(js) 
        for i in range(2): # 2번 스크롤 내리기
            await page.wait_for_timeout(3000) # 3초 대기
            # window.scrollTo(시작위치,이동위치)
            # 이동위치 : document(현재HTML).body(본문).scrollHeight -) 즉 현제 브라우져 스크롤을 본문의 가장 하단으로 이동 
            await page.evaluate("window.scrollTo(0, document.body.scrollHeight)") # await page.evaluate(js코드)
            

        
        # (5) 실행된 페이지에서 특정한 요소 가져오기 
        # page.query_selector_all() : 여러개 , page.query_selector() : 한개 
        items = await page.query_selector_all('.tile_item') #  이거 띄어쓰기 주의 !
        
        image_list = [] 
        for item in items: # 여러개 item 에서 제목과 이미지 가져오기  
            
            title_tag = await item.query_selector('.info_title .txt') # 제목 
            title = await title_tag.inner_text() if title_tag else "제목 없음" # <마크업>inner_text<마크업>
            
            image_tag = await item.query_selector('img._fe_image_tab_content_thumbnail_image') # 이미지 
            image_link  = await image_tag.get_attribute('src') if image_tag else "이미지 없음" # <마크업 속성명=값> 
            
            image_list.append({'제목' : title, '링크' : image_link})
        
        print(image_list) # 이미지 제목과 링크 리스트
        
        # (*) (직접) 안전하게 브라우져 닫기 
        await browser.close()
        

asyncio.run(naverRun()) # 동기화된 함수 실행
        