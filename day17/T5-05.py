
# 동적 페이지 크롤링 

import asyncio
from playwright.async_api import async_playwright
import pandas as pd

# [1] 크롤링 페이지 
# https://web.joongna.com/search/코키콜라?page=1

async def joongnaRun():
    
    #[1] 브라우져 실행 
    async with async_playwright() as p: 
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
    
        # [4] 크롤링할 페이지 이동 
        await page.goto('https://web.joongna.com/search/코카콜라?page=1')
        
        # [5] 해당 페이지 모두 열렸을때까지 대기 , 시스템상태(인터넷속도)알수 없을때 
        # await page.wait_for_timeout(5000)  , .wait_for_load_state('특정상태) , networkidle : 통신이 모두 종료 상태 
        await page.wait_for_load_state('networkidle')
        
        # [5-1] 특정한 검색창 활용 
        await page.get_by_placeholder('최소 가격').fill('10000')
        await page.wait_for_timeout(1000) # 1초 대기
        
        await page.get_by_placeholder('최대 가격').fill('20000')
        await page.wait_for_timeout(1000) # 1초 대기
        
        # 버튼 클릭 이벤트  , 특정한 식별자가 없는 경우에 버튼에 보이는 이름으로 가져올수 있다 . 
        apply_button = page.get_by_role('button',name='적용') # 버튼 클릭 이벤트
        await apply_button.click() # 버튼 클릭 이벤트
        await page.wait_for_load_state('networkidle') # 버튼 클릭후 페이지가 모두 열릴때까지 대기
        
        
        # [6] 특정한 요소 가져오기 
        # 선택자 : a['href="/링크/"']
        items = await page.query_selector_all('div.group> div > a[href^="/product/"]') # 여러개 요소 가져오기
        
        # [7] 제품명과 가격 추출 
        for item in items:
            title_tag = await item.query_selector('span.whitespace-pre-line')
            title = await title_tag.inner_text() if title_tag else "제목 없음"
            print(title)
            
            price_tag = await item.query_selector('span.text-18')
            price = await price_tag.inner_text() if price_tag else 0
            print(price)
            
            item = {'제품명' : title, '가격' : price}
            print(item)
        
        

# 동기함수 실행 
asyncio.run(joongnaRun())

