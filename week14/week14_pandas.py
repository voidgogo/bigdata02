import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pr = pd.read_csv('product.csv')
# print(pr.head(20))
pr['path'] = pr.groupby('product_id')['operator'].transform(
    lambda x: '_'.join(x)
)
pr['path'] = pr['factory'] + '_' + pr['path']
pr = pr.drop_duplicates('product_id')
pr = pr[['date', 'product_id', 'passfail', 'path']]
# print(pr.head())
pr['factory'] = pr['path'].map(lambda x: x[0:2])  # 팩토리 코드만 추출
# print(pr.tail())
pr['path'] = pr['path'].map(lambda x: x[3:])  # 3열 부터 끝까지 추출
# print(pr.tail())
pr['path'] = pr['path'].map(lambda x: x.split('_'))  # 언더스코어 기준으로 분리해서 리스트로 리턴
# print(pr.tail())
pr = pr.explode('path')  # path 칼럼의 데이터를 행으로 분리 (1->3)
# print(pr.tail(15))
# print(pr)
process_map = {
    '1':'P1',
    '2':'P1',
    'V':'P2',
    'W':'P2',
    'X':'P3',
    'Y':'P3'
}
pr['process'] = pr['path'].map(process_map)
# print(pr)
pr = pr.rename({'path':'operator'}, axis=1)
print(pr)