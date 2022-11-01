from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
# pd.set_option('display.max_rows', None)
import numpy as np  # linear algebra
import pandas as pd  # data processing

df = pd.read_csv("Chicagodata.csv")
print(df.head(1))
print('Data Frame Size: ', df.count())
list_of_column_names = list(df.columns)
# displaying the list of column names
print('List of column names : ', list_of_column_names)

#  maybe rounding the decimal place of location to 5th place gives to 1m accuracy
df['Latitude'] = df['Latitude'].round(decimals=4)
df['Longitude'] = df['Longitude'].round(decimals=4)
print(df)
#  df.round({"Latitude": 5, "Longitude": 5, "Location": 5})
print('Number of unique latitudes: ', len(df.Latitude.unique()))
print('Number of unique longitudes: ', len(df.Longitude.unique()))
print('Number of unique locations: ', len(df.Location.unique()))
print('Number of Descriptions: ', len(df.Description.unique()))

print('Description of Location Data: ', df['Location'].describe())

print(df.sort_values(by=['Latitude', 'Longitude'], ascending=False).head(2))

sorted_df = df.sort_values(by=["Domestic"], ascending=False)
print('list of sorted : ', sorted_df)

# group by domestic, apply average to x coordinate
# df1 = df.groupby('Domestic')['X Coordinate'].apply(np.average)
# print(df1.head())

df.rename(columns={"Primary Type": "primary_type"}, inplace=True)
print(df.columns)

# group by primary type of crime, ascending order
count_series = df.groupby(['primary_type']).size().sort_values(ascending=False)
# want to also include a column for during covid phase
# count_series = df.loc[df['Covid phase'] == 'Lockdown and restricted Period']
print(count_series)

# locate = df.loc[(df['primary_type'] == 'BATTERY') & (df['Description'] == 'DOMESTIC BATTERY SIMPLE')]
# print(locate)
# domestic_assault = df.groupby(['primary_type', 'Domestic' == 'DOMESTIC BATTERY SIMPLE'])
# print(domestic_assault)
