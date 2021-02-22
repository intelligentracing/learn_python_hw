import os
import datetime
import numpy as np 
import math
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

#读取文件
path = os.path.dirname(os.path.abspath(__file__))
source_filename = 'AAPL_M4.csv'
source_handle = open(path+'/'+source_filename,'r')

#将文件中的日期和收盘价作为键值对存放在closing_price_dictionary中
closing_price_dictionary = dict()
for line in source_handle.readlines()[1:]:
    line_list = line.split(',')
    closing_price_dictionary[line_list[0]] = line_list[6]

#将字符串格式的日期转换为日期格式，
# 解决股市周末不开盘总天数达不到365天的问题
start = ''
key_list = [] 
#用于区分start日期和之后的日期
n = 0
for key,value in closing_price_dictionary.items():
    if n == 0:
        start = datetime.datetime.strptime(key,'%Y-%m-%d')
        key_list.append(n) 
        n += 1
    else:
        current = datetime.datetime.strptime(key,'%Y-%m-%d')
        diff = current - start
        key_list.append(diff.days)

x = np.array(key_list).reshape(-1, 1)
#print(X.shape)
y = np.array(list(closing_price_dictionary.values()))
#print(y.shape)
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LinearRegression()
model.fit(x, y)

print('模型系数a: ',model.coef_)
print('模型截距b: ',model.intercept_)
  
y_pred = model.predict([[365]])
y_pred_30 = model.predict([[365+30]])
print('今天的股价是：',y_pred)
print('30天之后的股价是: ', y_pred_30)
rms = mean_squared_error(np.array(y[-1]), y_pred)
#预测数据与原始数据均值之差的平方和/原始数据和原始数据均值之差的平方和
#print('模型的衡量指标Squared：',rms)



