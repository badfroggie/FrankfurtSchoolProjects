import matplotlib.pyplot as plt
import pandas as pd

crimes = {
    'Hour': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
             14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
    'Domestic': [15077, 9840, 8481, 6964, 5651, 4763, 4840, 6539, 8707,
                 10472, 10509, 10468, 11527, 9518, 9631, 10357, 10684,
                 11020, 11315, 11368, 11722, 11973, 12573, 12132],
    'Total': [74422, 40933, 35330, 29176, 23476, 20453, 23156, 31645,
              45434, 60179, 59983, 61142, 80855, 63825, 66889, 72226,
              70535, 72129, 73181, 72186, 69034, 63577, 62037, 53440]
}

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
df2 = pd.DataFrame(crimes)
df2.plot(x='Hour',
         ylabel='Number of Crimes',
         rot=0, color={"Total": "gray", "Domestic": "black"},
         kind='bar', stacked=True,
         title='Total Crime and Domestic Crimes, per hour')
plt.show()


df2['Perc_Domestic'] = (df2['Domestic'] / df2['Total']) * 100

fig, ax = plt.subplots()
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
            14, 15, 16, 17, 18, 19, 20, 21, 22, 23])
# axes = df2.plot.line(subplots=True)
df2.plot(x='Hour', y='Perc_Domestic',
         xlabel='Hour',
         ylabel='Percentage of Domestic vs Total Crimes',
         title='Percent of Domestic vs Total Crimes per hour', ax=ax)
# type(axes)
plt.show()


df2['Perc_Domestic'] = (df2['Domestic'] / df2['Total']) * 100
print(df2)