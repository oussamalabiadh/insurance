# -*- coding: utf-8 -*-
"""insurance.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10HRfMUSG4PSKd2N-m3C2gLMciJ1bq2Z-

1- read dataset

2- explore data

3-visulization data

4- data preprocessing

5- split data

6- linear regression model

7- evaluate model
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('insurance.csv')

df.head()

df.shape

df.describe()

df.info()

sns.pairplot(df) #visualisation of total data

def pie_plot(column):
  fig,ax =plt.subplots()
  ax.pie(df[column].value_counts(),autopct="%0.2f%%", labels =df[column].value_counts().index)
  ax.set(title = f"pie chart of {column}")

columns =["sex" , "smoker","region"]
for column in columns:
  pie_plot(column)

mapper_sex = {"male":0,"female":1}
df['sex'] = df['sex'].map(mapper_sex)
df.head()

mapper_smoker = {"yes":1,"no":0}
df['smoker'] = df['smoker'].map(mapper_smoker)
df.head()

df['region'].unique()

mapper_region = {"southwest":0,"southeast":1,"northwest":2,"northeast":3}
df['region'] = df['region'].map(mapper_region)
df.head()

x= df.drop('charges',axis=1)

x.head()

y= df['charges']

y.head()

#split data intotrain andtest
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=24)

print("x_train size =",x_train.shape)
print("x_test size =",x_test.shape)
print("y_train size =", y_train.shape)
print("y_test size =", y_test.shape)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.fit_transform(x_test)

from sklearn.linear_model import LinearRegression

#call linear regression
lr_model=LinearRegression()

#fit model on the train data
lr_model.fit(x_train,y_train)

#predict value
y_pred=lr_model.predict(x_test)

from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

print("MAE =",mean_absolute_error(y_test,y_pred))

print("MSE =",mean_squared_error(y_test,y_pred))

print("RMSE =",np.sqrt(mean_squared_error(y_test,y_pred)))

print("R Squared Error = " , r2_score(y_test,y_pred))

