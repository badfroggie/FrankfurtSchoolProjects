import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("Chicagodata.csv")
df.rename(columns={"Primary Type": "primary_type"}, inplace=True)
df.rename(columns={"Covid phase": "covid_phase"}, inplace=True)
df.rename(columns={"Location Description": "location_des"}, inplace=True)
df_filtered = df[(df['covid_phase'] == 'Lockdown and restricted Period') & ~(df['location_des'] == 'RESIDENCE')]
print('Number of unique locations: ', len(df_filtered.Location.unique()))
print(df_filtered.head(5))
print(df_filtered.shape)
print('Description of Location Data: ', df_filtered['Location'].describe())
color_map = plt.cm.get_cmap('YlOrBr')
# make a new column in pandas, returns color
color_dict = pd.Series({k: color_map(np.random.rand()) for k in df_filtered['primary_type'].unique()})
color_dict.name = 'color_dict'
df_filtered = pd.merge(df_filtered, color_dict, how='left', left_on='primary_type', right_index=True)
# create scatter plot, fitted to the data
ax1 = df_filtered.plot.scatter(x='Longitude', xlim=(-87.4, -88.1),
                      y='Latitude', ylim=(41.5, 42.2),
                      s=0.02,
                      c=df_filtered['color_dict'],
                      figsize=(7, 7),
                      title='Crime Map of Chicago During Lockdown, Location Description = Residence')
# adding point of top location crime occurs
ax1.plot(-87.709271389, 41.868180939, "or")
plt.show()
# deleting the other covid phases
# index_phase = df[(df['covid_phase'] == 'Before Covid') & (df['covid_phase'] == 'Post Covid')].index
# df.drop(index_phase, inplace=True)
# print(df.head(5))
# print(df.shape)
