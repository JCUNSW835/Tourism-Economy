import numpy as np
import pandas as pd
import pandasql as ps
import matplotlib.pyplot as plt
import seaborn as sns

# load csv file 
df = pd.read_csv('Regions-by-traveller-type.csv')
# Rename the column names for convenience
df.rename({'Year-ending-December-2019' : 'visitor_19'}, axis=1, inplace=True)

# Use the sql code to extract relevant info from the csv file
# Year for this py is 2019 and 2020
# 11 Regions will be select to compare GVA in NSW: no sydney and outback NSW
# use group by to add all numbers by regions
# remember the number is in (000s)

dfs = ps.sqldf ("SELECT Region, visitor_19"
 + " From df " 
 + " WHERE Region = 'Capital Country' or Region = 'Blue Mountains' or Region = 'Central Coast' or Region = 'Central NSW' or Region = 'Hunter' or Region = 'New England North West' or Region = 'Central Coast' or Region = 'North Coast NSW' or Region = 'Riverina' or Region = 'Snowy Mountains' or Region = 'South Coast' or Region = 'The Murray' "
 + " GROUP BY Region"
)

print(dfs)

sns.set()
sns.set_context("paper")

# Converting string to float so that sns can red the visitor19 data

dfs = dfs.explode('visitor_19')
dfs['visitor_19'] = dfs['visitor_19'].astype('float')

# Start ploting the graph, use the seaborn to draw bar graph with x =region and y = visitor_19
fig, ax = plt.subplots()
ax = sns.barplot(x="Region", y="visitor_19", data=dfs,
                saturation=.3, palette=['Steelblue', 'Steelblue', 'Steelblue','Steelblue','Salmon','Steelblue','Salmon','Red','Red','Salmon','Red']) 

# set color to the top three bar and the last one
# change the color for the bottom three to another indicating comparision ####
# for bar in ax.patches:
#    if bar.get_height() > 8300 or bar.get_height() < 2900:
#        bar.set_color('salmon')     
#    else:
#        bar.set_color('steelblue')


#display numbers on the top of bars
for index, row in dfs.iterrows():
 ax.text(row.name,row.visitor_19, round(row.visitor_19,3), color='black', ha="center", fontsize=18)

# Format the bar graph by adding x,y labels and a title
# Change the rotation to 50 so that people can read the name of regions
# Change the size of whole pictures allow whole bar graph to git in
plt.title("2019 Total Visitors('000) in 11 Regions", fontsize=40)
plt.xlabel("Regions", fontsize=25)
plt.ylabel("Visitors ('000)", fontsize=25)
plt.xticks(rotation=50, fontsize=18)
plt.yticks(fontsize=18)
plt.gcf().set_size_inches(16, 30)


# Show the bar graph and save as 2019-visitor
plt.show()
plt.savefig('2019-visitor.png')                