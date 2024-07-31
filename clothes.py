import pandas as pd
import matplotlib.pyplot as plt
import pymysql


conn = pymysql.connect(
    host='3.35.133.116',
    user='clouds2024',
    password='clouds2024',
    db='clouds2024',
    charset='utf8mb4'
)


query = """
SELECT 
    AVG(니트_스웨터) AS knit_sweater,
    AVG(카디건) AS cardigan,
    AVG(원피스) AS dress,
    AVG(티셔츠) AS tshirt,
    AVG(블라우스_셔츠) AS blouse_shirt,
    AVG(점퍼) AS jumper,
    AVG(재킷) AS jacket,
    AVG(코트) AS coat,
    AVG(바지) AS pants,
    AVG(청바지) AS jeans,
    AVG(스커트) AS skirt,
    AVG(레깅스) AS leggings,
    AVG(트레이닝복) AS training_suit,
    AVG(조끼) AS vest,
    AVG(정장세트) AS suit_set,
    AVG(한복) AS hanbok,
    AVG(유니폼_단체복) AS uniform,
    AVG(파티복) AS party_dress,
    AVG(레인코트) AS raincoat,
    AVG(점프슈트) AS jumpsuit,
    AVG(코디세트) AS coordination_set
FROM clothing_data
WHERE 날짜 BETWEEN '2023-08-01' AND '2023-09-30';
"""
df = pd.read_sql_query(query, conn)

# 데이터베이스 연결 종료
conn.close()

# 평균 값을 시각화
plt.figure(figsize=(14, 7))
plt.bar(df.columns, df.iloc[0], color='skyblue')
plt.xticks(rotation=90)
plt.xlabel('Clothing Items')
plt.ylabel('Average Count')
plt.title('Average Count of Clothing Items from 2023-08-01 to 2023-09-30')
plt.show()
