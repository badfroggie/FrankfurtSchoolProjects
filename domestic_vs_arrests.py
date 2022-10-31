import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("Chicagodata.csv")
df.rename(columns={"Primary Type": "primary_type"}, inplace=True)
df.rename(columns={"Covid phase": "covid_phase"}, inplace=True)
df.rename(columns={"Location Description": "location_des"}, inplace=True)
df.rename(columns={"Case Number": "case_number"}, inplace=True)

# print('Data Frame Size: ', df.count())
total_crimes = len(df)
print('Total number of Crimes in 2017-2022:', total_crimes)

count = df['Domestic'].sum()
print('Count of True values in Column Domestic\nNumber of domestic crimes: ', count)

rate_of_domestic = (count / total_crimes) * 100
print("Percentage of Domestic Crimes: ", rate_of_domestic)

c17 = len(df[df['Year'] == 2017])
c18 = len(df[df['Year'] == 2018])
c19 = len(df[df['Year'] == 2019])
c20 = len(df[df['Year'] == 2020])
c21 = len(df[df['Year'] == 2021])
c22 = len(df[df['Year'] == 2022])
print("Number of crimes in 2017-2022:", c17, ", ",
      c18, ", ",
      c19, ", ",
      c20, ", ",
      c21, ", ",
      c22)

total_crimes_added = c17 + c18 + c19 + c20 + c21 + c22
print("Total crimes, checked by adding crimes/year: ", total_crimes_added)

df_filt2017 = df.loc[(df['Year'] == 2017) & (df['Domestic'] == True), 'Domestic'].sum()
df_filt2018 = df.loc[(df['Year'] == 2018) & (df['Domestic'] == True), 'Domestic'].sum()
df_filt2019 = df.loc[(df['Year'] == 2019) & (df['Domestic'] == True), 'Domestic'].sum()
df_filt2020 = df.loc[(df['Year'] == 2020) & (df['Domestic'] == True), 'Domestic'].sum()
df_filt2021 = df.loc[(df['Year'] == 2021) & (df['Domestic'] == True), 'Domestic'].sum()
df_filt2022 = df.loc[(df['Year'] == 2022) & (df['Domestic'] == True), 'Domestic'].sum()
print("Number of Domestic Crimes per Year: ",
      "\n2017: ", df_filt2017,
      "\n2018: ", df_filt2018,
      "\n2019: ", df_filt2019,
      "\n2020: ", df_filt2020,
      "\n2021: ", df_filt2021,
      "\n2022: ", df_filt2022)

rod17 = (df_filt2017 / c17) * 100
rod18 = (df_filt2018 / c18) * 100
rod19 = (df_filt2019 / c19) * 100
rod20 = (df_filt2020 / c20) * 100
rod21 = (df_filt2021 / c21) * 100
rod22 = (df_filt2022 / c22) * 100
print("Percentage of Domestic Crimes per Year: ",
      "\n2017: ", rod17,
      "\n2018: ", rod18,
      "\n2019: ", rod19,
      "\n2020: ", rod20,
      "\n2021: ", rod21,
      "\n2022: ", rod22,)

dcpy = {
    'Year': [2017, 2018, 2019, 2020, 2021, 2022],
    'Domestic': [df_filt2017, df_filt2018, df_filt2019, df_filt2020, df_filt2021, df_filt2022],
    'Total': [c17, c18, c19, c20, c21, c22],
}
df2 = pd.DataFrame(dcpy)
print(df2)

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
df2 = pd.DataFrame(dcpy)
df2.plot(x='Year',
         ylabel='Number of Crimes',
         rot=0, color={"Total": "gray", "Domestic": "black"},
         kind='bar', stacked=True,
         title='Total Crime and Domestic Crimes, per Year')
plt.show()

df2['Perc_Domestic'] = (df2['Domestic'] / df2['Total']) * 100
print(df2)

plt.figure(figsize=(8, 8))
colors_list = ['Purple']
graph = plt.bar(df2.Year, df2.Domestic, color=colors_list)
plt.title('Percentage of Domestic')

i = 0
for p in graph:
    width = p.get_width()
    height = p.get_height()
    x, y = p.get_xy()
    plt.text(x+width/2,
             y+height*1.01,
             str(df2.Perc_Domestic[i])+'%',
             ha='center',
             weight='bold')
    i += 1
plt.show()
