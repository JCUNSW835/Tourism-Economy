import pandas as pd
import pandasql as ps
import openpyxl
import matplotlib.pyplot as plt
import seaborn as sns
selected_data = pd.read_csv('5locations.csv', index_col=False)
dfs = pd.DataFrame(selected_data)

Change_Exp = ps.sqldf(
    " SELECT Regions, Year, Total "
+   " FROM dfs "
+   " WHERE Year != 'Year ending December 2019' AND Year != 'Year ending December 2020' "
)

print(Change_Exp)

fig, ax = plt.subplots()
sns.set()
sns.set_context("paper")
bar = sns.catplot(x="Year", y="Total", hue="Regions", kind="bar", data = Change_Exp, palette = "coolwarm")

plt.title("Percentage of Change of Total Expenditures ($M) From 2019 To 2020", fontsize=12, pad=1)
plt.xticks(rotation=0)
plt.xlabel("Year", fontsize=12)
plt.ylabel("% Change of Total Expenditures ($M)", fontsize=12)
plt.gcf().set_size_inches(9,8)
plt.margins(0.2)


# display the graph
plt.show()
plt.savefig("% Change of Total Expenditures From 2019 To 2020.png")