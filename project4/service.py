import pandas as pd
import time
import matplotlib.pyplot as plt
import seaborn 
import koreanfont

class DataService:
    def __init__(self):
        self.data = pd.read_csv("yes24_bestseller.csv")

        # 전처리
        self.data["가격"] = (
            self.data["가격"].str.replace(",", "").str.replace("원", "").astype(int)
        )
        # self.data['년'] = self.data['출판년월'].str[:4]
        # self.data['월'] = self.data['출판년월'].str[6:8]
        self.data["출판년월"] = pd.to_datetime(
            self.data["출판년월"], format="%Y년 %m월"
        )
        self.data["년"] = self.data["출판년월"].dt.year
        self.data["월"] = self.data["출판년월"].dt.month

        print(self.data.head())
        print(self.data.dtypes)

    # 평균 가격
    def get_stat(self):
        stat = {"평균가격": self.data["가격"].mean(), "최고가격": self.data['가격'].max(), "최저가격": self.data['가격'].min(), "최다출판연도": self.data['년'].mode()[0]}
        print(stat)
        return stat

    # 연도별 도서수 
    def book_count(self) : 
        bc = self.data['년'].value_counts()
        # print(bc)
        return bc
    
    # 시각화 
    def visual(self) : 
        # 가격대별 도서수 
        plt.figure()
        self.data['가격'].hist()
        plt.xlabel('가격대')
        plt.ylabel('도서수')
        
        # 연도별 도서수 막대 
        plt.figure()
        bc = self.book_count()
        plt.bar(bc.index , bc.values)
        plt.xlabel('연도')
        plt.ylabel('도서수')        
        plt.show()
        


# 객체 생성
data_service = DataService()
# data_service.get_stat()
# data_service.book_count()
data_service.visual()



# 5. REST API 기능 (FastAPI)
#   1. 통계 데이터 조회 API . GET /stats
#   2. 반환 데이터
#     가. 평균 가격
#     나. 최고 가격
#     다. 최저 가격
#     라. 가장 많이 출판된 연도
#   3. 응답 예시
# {   "평균가격": 17200,
#     "최고가격": 45000,
#     "최저가격": 5900,
#     "최다출판연도": 2024  }
