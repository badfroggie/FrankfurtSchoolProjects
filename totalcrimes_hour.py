import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Chicagodata.csv")
# df['hour'] = df.Date.str.extract("(^\d+):", expand=False)
df['hour'] = pd.to_datetime(df['Date']).dt.hour
list_of_column_names = list(df.columns)
print(df)
print(list_of_column_names)

# df_filter = df.loc[(df['Domestic'] == True), 'Domestic'].sum()
# print(df_filter)

count_series = df.groupby(['hour']).size().sort_values(ascending=False)
print(count_series)

new_df = df.groupby(['hour']).size().to_frame('# of Total Crimes').reset_index()
print(new_df)

new_df.plot(kind='bar', x='hour',
            xlabel='Hour',
            ylabel='number of crimes',
            color='gray',
            title='Crimes per Hour', figsize=(7, 3.5))
plt.show()




