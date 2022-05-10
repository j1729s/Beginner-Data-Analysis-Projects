Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> import pandas as pd
>>> import matplotlib.pyplot as plt
>>> import seaborn as sns
>>> import warnings
>>> warnings.filterwarnings('ignore')
>>> df = pd.read_csv (r'C:\Users\suer\Downloads\IRIS.csv')
>>> df.head()
   sepal_length  sepal_width  petal_length  petal_width      species
0           5.1          3.5           1.4          0.2  Iris-setosa
1           4.9          3.0           1.4          0.2  Iris-setosa
2           4.7          3.2           1.3          0.2  Iris-setosa
3           4.6          3.1           1.5          0.2  Iris-setosa
4           5.0          3.6           1.4          0.2  Iris-setosa
>>> df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 5 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   sepal_length  150 non-null    float64
 1   sepal_width   150 non-null    float64
 2   petal_length  150 non-null    float64
 3   petal_width   150 non-null    float64
 4   species       150 non-null    object 
dtypes: float64(4), object(1)
memory usage: 5.3+ KB
>>> df.describe()
       sepal_length  sepal_width  petal_length  petal_width
count    150.000000   150.000000    150.000000   150.000000
mean       5.843333     3.054000      3.758667     1.198667
std        0.828066     0.433594      1.764420     0.763161
min        4.300000     2.000000      1.000000     0.100000
25%        5.100000     2.800000      1.600000     0.300000
50%        5.800000     3.000000      4.350000     1.300000
75%        6.400000     3.300000      5.100000     1.800000
max        7.900000     4.400000      6.900000     2.500000
>>> sns.pairplot(df, hue='species')
<seaborn.axisgrid.PairGrid object at 0x12AB5E30>
>>> plt.show()
>>> grouped = df.groupby(df.species)
>>> df1 = grouped.get_group("Iris_setosa")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    df1 = grouped.get_group("Iris_setosa")
  File "C:\Users\suer\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\groupby\groupby.py", line 810, in get_group
    raise KeyError(name)
KeyError: 'Iris_setosa'
>>> df1 = grouped.get_group("Iris-setosa")
>>> df2 = grouped.get_group("Iris-virginica")
>>> df3 = grouped.get_group("Iris-versicolor")
>>> df1['sepal_length'].hist()
<AxesSubplot:>
>>> plt.show()
>>> 
