import pandas as pd

#import data from csv file
df_weight = pd.read_csv('data/weight.csv', delimeter=',',header='infer')
df_weight.head()

df_weight