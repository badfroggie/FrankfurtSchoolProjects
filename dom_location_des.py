import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Chicagodata.csv")
print(df.head(1))
print('Data Frame Size: ', df.count())
list_of_column_names = list(df.columns)
# displaying the list of column names
print('List of column names : ', list_of_column_names)

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

sorted_df = df.sort_values(by=["location_des"], ascending=False)
count_series = df.groupby(['location_des']).size().sort_values(ascending=False)
print('list of sorted : ', count_series.head(15))

street = len(df[df['location_des'] == 'STREET'])
residence = len(df[df['location_des'] == 'RESIDENCE'])
apartment = len(df[df['location_des'] == 'APARTMENT'])
sidewalk = len(df[df['location_des'] == 'SIDEWALK'])
retail = len(df[df['location_des'] == 'SMALL RETAIL STORE'])
other = len(df[df['location_des'] == 'OTHER'])
restaurant = len(df[df['location_des'] == 'RESTAURANT'])
alley = len(df[df['location_des'] == 'ALLEY'])
parking = len(df[df['location_des'] == 'PARKING LOT/GARAGE(NON.RESID.)'])
vehicle = len(df[df['location_des'] == 'VEHICLE NON-COMMERCIAL'])
print("Number of crimes in a location type:", street, ", ",
      residence, ",",
      sidewalk, ", ",
      apartment, ", ",
      retail, ", ",
      other, ", ",
      restaurant, ", ",
      alley, ", ",
      parking, ", ",
      vehicle
      )

top_10_crimes_loc_added = (street + residence + sidewalk + apartment + retail + other
                           + restaurant + alley + parking + vehicle)
print("Total crimes, checked by adding crimes/location description: ", top_10_crimes_loc_added)


df_street_dom = df.loc[(df['location_des'] == 'STREET') & (df['Domestic'] == True), 'Domestic'].sum()
df_res_dom = df.loc[(df['location_des'] == 'RESIDENCE') & (df['Domestic'] == True), 'Domestic'].sum()
df_apartment_dom = df.loc[(df['location_des'] == 'APARTMENT') & (df['Domestic'] == True), 'Domestic'].sum()
df_sidewalk_dom = df.loc[(df['location_des'] == 'SIDEWALK') & (df['Domestic'] == True), 'Domestic'].sum()
df_retail_dom = df.loc[(df['location_des'] == 'SMALL RETAIL STORE') & (df['Domestic'] == True), 'Domestic'].sum()
df_other_dom = df.loc[(df['location_des'] == 'OTHER') & (df['Domestic'] == True), 'Domestic'].sum()
df_restaurant_dom = df.loc[(df['location_des'] == 'RESTAURANT') & (df['Domestic'] == True), 'Domestic'].sum()
df_alley_dom = df.loc[(df['location_des'] == 'ALLEY') & (df['Domestic'] == True), 'Domestic'].sum()
df_parking_dom = df.loc[(df['location_des'] == 'PARKING LOT/GARAGE(NON.RESID.)') & (df['Domestic'] == True), 'Domestic'].sum()
df_vehicle_dom = df.loc[(df['location_des'] == 'VEHICLE NON-COMMERCIAL') & (df['Domestic'] == True), 'Domestic'].sum()

print("Number of Domestic Crimes per location description: ",
      "\nstreet: ", df_street_dom,
      "\nresidence: ", df_res_dom,
      "\napartment: ", df_apartment_dom,
      "\nsidewalk: ", df_sidewalk_dom,
      "\nretail store: ", df_retail_dom,
      "\nother: ", df_other_dom,
      "\nrestaurant: ", df_restaurant_dom,
      "\nalley: ", df_alley_dom,
      "\nparking lot: ", df_parking_dom,
      "\nvehicle: ", df_vehicle_dom
      )

rod_street = (df_street_dom / street) * 100
rod_residence = (df_res_dom / residence) * 100
rod_apartment = (df_apartment_dom / apartment) * 100
rod_sidewalk = (df_sidewalk_dom / sidewalk) * 100
rod_retail = (df_retail_dom / retail) * 100
rod_other = (df_other_dom / other) * 100
rod_restaurant = (df_restaurant_dom / restaurant) * 100
rod_alley = (df_alley_dom / alley) * 100
rod_parking = (df_parking_dom / parking) * 100
rod_vehicle = (df_vehicle_dom / vehicle) * 100
print("Percentage of Domestic Crimes per location description: ",
      "\nstreet: ", rod_street,
      "\nresidence: ", rod_residence,
      "\napartment: ", rod_apartment,
      "\nsidewalk: ", rod_sidewalk,
      "\nretail store: ", rod_retail,
      "\nother: ", rod_other,
      "\nrestaurant: ", rod_restaurant,
      "\nalley: ", rod_alley,
      "\nparking lot: ", rod_parking,
      "\nvehicle: ", rod_vehicle
      )

dom_locations = {
    'Locations': ['street', 'residence', 'apartment', 'sidewalk', 'retail',
                  'other', 'restaurant', 'alley', 'parking', 'vehicle'],
    'Percent of Domestic': [rod_street, rod_residence, rod_apartment, rod_sidewalk, rod_retail, rod_other,
                            rod_restaurant, rod_alley, rod_parking, rod_vehicle]
}

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
df2 = pd.DataFrame(dom_locations)
df2.plot(x='Locations',
         ylabel='Percent Domestic',
         rot=30, color={"Percent of Domestic": "gray"},
         kind='bar', stacked=True,
         title='Percent Domestic Crimes per Location Type')
plt.show()
