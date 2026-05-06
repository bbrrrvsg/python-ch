import numpy as np

data = np.genfromtxt(
    './numpyproject/tbsh_gyeonggi_day_202512_안양시.csv',
    delimiter=',',
    encoding='utf-8-sig', # 각 csv 마다의 인코딩 타입 맞춤
    skip_header=1,
    dtype=str   # 서로 다른 타입이라서 모두 str 로 변경 
)
print(data.shape)



# Step 3: 위기/효율 지수 산출 (Broadcasting)
# 미션: 고령층 매출 건수 / 의료 업종 매출 건수 연산을 통해 '의료 결핍 지수' 배열을 생성하고, 
# 이 지수가 가장 높은 행정동코드(admi_cty_r)를 찾으세요. 

고령층매출건수조건 = data[:,8] >= "06"
고령층매출건수 = data[고령층매출건수조건,11].astype(float)

의료업종매출건수조건 = data[:,4] == "의료/건강" 
의료업종매출건수 = data[의료업종매출건수조건,11].astype(float)
print(의료업종매출건수)

print(np.unique(data[:,2]))




# 의료결핍지수조건 = 고령층매출건수 / 의료업종매출건수


# 의료결핍지수 = 

# 분석 결과: 해당 고객/대상 ID (                )

# 의미: 어르신들의 활동량 대비 의료 인프라가 얼마나 턱없이 부족한지를 수치화하여, 
# 상대적으로 가장 관리가 시급한 '워스트 케이스' 동네를 특정합니다. 






# Step 5: 상대적 우선순위 결정 (Normalization)
# 미션: '의료 결핍 지수'를 0~1 사이로 정규화(Min-Max Scaling)하고, 최종 점수가 0.9 이상인 '최우선 관리 행정동'의 코드를 추출하세요. 
# 분석 결과: 대상자 수 (                ) 명
# 의미: 예산과 자원은 한정되어 있으므로, 정규화된 점수를 바탕으로 가장 먼저 '이동식 보건소'나 '실버 셔틀'을 투입해야 할 곳을 결정하는 객관적 근거를 마련합니다. 
