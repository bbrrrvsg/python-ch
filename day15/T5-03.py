
import pandas as pd 
import matplotlib.pyplot as plt 
import koreanfont
import json 

# [1] Ts_data.json 파일내 patient_status_data 
with open( './T5_data.json' , 'r' , encoding='utf-8') as json_file :
    data_josn = json.load(json_file)
df = pd.DataFrame(data_josn['patient_status_data'])
print(df)

# [2] 막대차트 : 상태별 환자수 비교 
# plt.bar(x축값,y축값)
plt.bar(df['상태'],df['환자 수'])
plt.title('상태별 환자수 비교')
plt.xlabel('상태')
plt.ylabel('환자수')
plt.show()


# [3] 원형차트 : 전체대비 각 상태의 환자수 비율 
# plt.pie(값, )
plt.pie(df['환자 수'], labels=df['상태'] , autopct='%.2f%%' , startangle=90)
plt.title('환자상태비율')
plt.show()