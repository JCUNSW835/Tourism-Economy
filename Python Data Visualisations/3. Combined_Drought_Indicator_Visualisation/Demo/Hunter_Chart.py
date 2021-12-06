import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_excel("Concatenated_data.xlsx")
df["Date"]=pd.to_datetime(df["Date"])
df=df[df["Date"]=="31/08/2021"]
filtered_df=df[df["regionname"]=="HUNTER"]
sns.set_style("darkgrid")
ax=sns.countplot(x="CDI",hue="lganame",palette=sns.color_palette("Paired"),linestyle = "-.",linewidth = .5,edgecolor = "white",data=filtered_df)
plt.sca(ax)
plt.xlabel("CDI",fontweight='bold')
plt.ylabel("Count of Postcode Area",fontweight='bold')
plt.title("Distribution of CDI in Hunter Region",fontsize=12, fontweight='bold')
ax.set_xticklabels(("CDI=3 Weakening","CDI=5 Non Drought"))
for container in ax.containers:
    ax.bar_label(container)
plt.legend(title="LGA",loc='upper left',prop={'size': 8})
plt.tight_layout()
plt.savefig("CDI_hunter",dpi=1100)
