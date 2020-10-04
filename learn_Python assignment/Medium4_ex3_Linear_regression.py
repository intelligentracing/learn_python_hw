import os
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

path = os.path.dirname(os.path.abspath(__file__))
source_filename = 'AAPL_M4.csv'
source_handle = open(path+'/'+source_filename,'r')

closing_price_dictionary = dict()
for line in source_handle.readlines()[1:]:
    line_list = line.split(',')
    closing_price_dictionary[line_list[6]] = line_list[0]

 
y_sample = np.zeros(365)
A_sample = np.zeros((365, 2))

key_list = [] 
for key in closing_price_dictionary:
    for j in range(365):
        key_list.append(key) 
        A_sample[j] = [j,1]
for i in range(len(key_list)-365, len(key_list)):
    for k in range(365):
        y_sample[k] = key_list[i]

X = np.array(key_list[-365:]).reshape(-1, 1)
print(X.shape)
y = y_sample.reshape(-1, 1)
print(y.shape)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
regressor = LinearRegression()
regressor.fit(X_train, y_train)

print(regressor.coef_)
print(regressor.intercept_)

y_pred = regressor.predict(X_test)

rms = sqrt(mean_squared_error(y_test, y_pred))
print(rms)

# aa = np.linalg.lstsq(A_sample, y_sample, rcond = None)[0]
# print(aa)

# def price_estimate(x):
#     return aa[0]*x + aa[1]

# print(price_estimate(395))
