import pandas as pd
import pandasql as ps
import openpyxl
import matplotlib.pyplot as plt
import seaborn as sns
selected_data = pd.read_csv('5locations.csv', index_col=False)
dfs = pd.DataFrame(selected_data)

Avg_Exp = ps.sqldf(
    " SELECT Regions, Year, Average "
+   " FROM dfs "
+   " WHERE Year = 'Year ending December 2019' OR Year = 'Year ending December 2020' "
)

print(Avg_Exp)

fig, ax = plt.subplots()
sns.set()
sns.set_context("paper")
bar = sns.catplot(x="Year", y="Average", hue="Regions", kind="bar", data = Avg_Exp, palette = "coolwarm")

plt.title("Average quarterly Expenditures ($M) 2019 v.s. 2020", fontsize=12, pad=1)
plt.xticks(rotation=0)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Avg Qtr Expenditures ($M)", fontsize=12)
plt.gcf().set_size_inches(9,8)
plt.margins(0.2)


# display the graph
plt.show()
plt.savefig("Avg Qtr Expenditures 2019 vs 2020.png")