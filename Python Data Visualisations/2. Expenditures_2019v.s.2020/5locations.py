import pandas as pd
import pandasql as ps
import openpyxl
import matplotlib.pyplot as plt
import seaborn as sns

# From the original dataset, select the specific sheet with data needed for this graph
data = pd.read_excel('Tourism Region Profiles Data Tables.xlsx', sheet_name='Regions by quarter', engine='openpyxl', index_col=False)
df = pd.DataFrame(data)
# df.to_csv('Regions by quarter.csv', index=False) # Save the sheet to a new csv file
df1 = df.set_axis(['Regions', 'Year', 'Q1($M)', 'Q2($M)', 'Q3($M)','Q4($M)'], axis=1, inplace=False)  # Rename the Column Names
df1 = df1.dropna(how="all") # Drop the missing values in the table
df1 = df1.drop(df1.index[[0,1]], axis=0) # Delete the first 2 rows which does not cover the table
# df1.to_csv('Renamed_columns.csv', index=False) # "index=False" meaning that the index column is not needed

# Filter out the 4 locations needed
Selected_locations = df1.loc[((df1['Regions'] == 'Hunter') | (df1['Regions'] == 'South Coast') | (df1['Regions'] == 'The Murray')| (df1['Regions'] == 'North Coast NSW')|(df1['Regions'] == 'Riverina'))]
# Hunter = df1.loc[df1['Regions'] == 'Hunter']
# SouthCoast = df1.loc[df1['Regions'] == 'South Coast']
# TheMurray = df1.loc[df1['Regions'] == 'The Murray']
# NorthCoastNSW = df1.loc[df1['Regions'] == 'North Coast NSW']
# Riverina = df1.loc[df['Regions] == 'Riverina']

# Filter out columns of Q1-Q4
df2 = Selected_locations.loc[:, ['Q1($M)','Q2($M)', 'Q3($M)','Q4($M)']]
# print(df2)
# Calculate average values for 2019 and 2020 in each location
avg_row = df2.mean(axis=1)
# print(avg_row)
# Calculate sum values for 2019 and 2020 in each location
sum_row = df2.sum(axis=1)
# print(sum_row)

# Insert the average and sum values for rows into Selected_locations
Selected_locations['Average'] = avg_row
Selected_locations['Total'] = sum_row

# Save them in a new csv file
Selected_locations.to_csv('5locations.csv', index=False)

selected_data = pd.read_csv('5locations.csv', index_col=False)
dfs = pd.DataFrame(selected_data)

Expenditures = ps.sqldf(
    " SELECT Regions, Year, Total "
+   " FROM dfs "
+   " WHERE Year = 'Year ending December 2019' OR Year = 'Year ending December 2020' "
)

print(Expenditures)

# Plot the graph using matplotlib.pyplot and seaborn
fig, ax = plt.subplots()
sns.set()
sns.set_context("paper")
bar = sns.catplot(x="Year", y="Total", hue="Regions", kind="bar", data = Expenditures, palette = "coolwarm")

plt.title("Total Expenditures ($M) 2019 v.s. 2020", fontsize=14, pad=1)
plt.xticks(rotation=0)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Total Expenditures ($M)", fontsize=12)
plt.gcf().set_size_inches(9,8)
plt.margins(0.2)

# display the graph
plt.show()
plt.savefig("Total Expenditures 2019 vs 2020.png")
