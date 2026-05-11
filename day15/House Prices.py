
import pandas as pd                 # 데이터표
import matplotlib.pyplot as plt     # 시각화1
import seaborn as sns               # 시각화2
import koreanfont                   # 한글폰트

# 지상 주거 면적 (GrLivArea)이 넓을수록 판매 가격은 정비례하여 상승할 것이다.

df = pd.read_csv( './day15/train_HousePrices.csv')
print(df.head())
df.info()
print( df.isnull().sum()[ df.isnull().sum() > 0 ] ) # 결측값 확인

# 1. 데이터 전처리 
# 1.1 수치형 변수 결측치 처리
df['LotFrontage'] = df['LotFrontage'].fillna( df['LotFrontage'].median() ) 
df['MasVnrArea'] = df['MasVnrArea'].fillna( df['MasVnrArea'].median() ) 
df['GarageYrBlt'] = df['GarageYrBlt'].fillna( df['GarageYrBlt'].median() ) 

# 1.2 범주형 변수 결측치 처리 (정보 부재 명확) , 특정 문자열로 대체
df['Alley'] = df['Alley'].fillna('NoAlley')
df['PoolQC'] = df['PoolQC'].fillna('NoPool')
df['Fence'] = df['Fence'].fillna('NoFence')

# 1.3 범주형 변수 결측치 처리 (일반) , 최빈값(Mode)을 활용하여 결측치를 일괄 보정

mode_cols = [
    'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2',
    'Electrical', 'FireplaceQu', 'GarageType', 'GarageFinish', 'GarageQual',
    'GarageCond', 'MSZoning', 'Functional', 'SaleType', 'Exterior1st', 
    'Exterior2nd', 'MasVnrType'
]

for i in mode_cols:
    df[i] = df[i].fillna(df[i].mode()[0])
    
print(df[mode_cols].isnull().sum())



# 2.1 주택 판매 가격(SalePrice) 분포 분석
# sns.histplot을 사용하여 주택 판매 가격(SalePrice)의 분포와 치우침(Skewness) 정도를 확인한다. (KDE 포함)

sns.histplot(df['SalePrice'],kde=True)
plt.title('주택 판매 가격(SalePrice) 분포')
plt.xlabel('가격')
plt.ylabel('빈도')
plt.show()

# 2.2 주거 면적과 가격 관계 분석 (가설 1 검증)
# sns.scatterplot을 사용하여 지상 주거 면적(GrLivArea)과 판매 가격(SalePrice) 간의 상관관계를 산점도로 분석한다.
# plt.scatter(x축 , y축 , s=원형크기(계산식) , alpha= 투명도 )

sns.scatterplot(x=df['GrLivArea'],y=df['SalePrice'],s=100,alpha=0.5)
plt.show()
