import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Chicagodata.csv")
df = df.loc[(df['Domestic'] == True)]
print(df)
df['hour'] = pd.to_datetime(df['Date']).dt.hour
list_of_column_names = list(df.columns)
print(df)
print(list_of_column_names)

# df_filter = df.loc[(df['Domestic'] == True), 'Domestic'].sum()
# print(df_filter)

count_series = df.groupby(['hour']).size().sort_values(ascending=False)
print(count_series)

new_df = df.groupby(['hour']).size().to_frame('# of DV Crimes').reset_index()
print(new_df)

new_df.plot(kind='bar', x='hour',
            color='gray',
            title='Domestic Crimes per Hour', figsize=(7, 3.5))
plt.show()
