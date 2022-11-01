import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import data from Chicago 2017-2022
df = pd.read_csv("Chicagodata.csv")
# rename primary type
df.rename(columns={"Primary Type": "primary_type"}, inplace=True)
# generate a color map
np.random.seed(seed=34)
color_map = plt.cm.get_cmap('YlOrBr')
# make a new column in pandas, returns color
color_dict = pd.Series({k: color_map(np.random.rand()) for k in df['primary_type'].unique()})
color_dict.name = 'color_dict'
df = pd.merge(df, color_dict, how='left', left_on='primary_type', right_index=True)
# create scatter plot, fitted to the data
ax1 = df.plot.scatter(x='Longitude', xlim=(-87.4, -88.1),
                      y='Latitude', ylim=(41.5, 42.2),
                      s=0.05,
                      c=df['color_dict'],
                      figsize=(7, 7),
                      title='Crime Map of Chicago 2017 to 2022')
# adding point of top location crime occurs
ax1.plot(-87.627876698, 41.883500187, "or")
plt.show()
