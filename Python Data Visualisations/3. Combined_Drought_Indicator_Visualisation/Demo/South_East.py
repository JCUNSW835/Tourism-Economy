import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("South Coast CDI.csv")
df["Date"]=pd.to_datetime(df["Date"])
df=df[df["Date"]=="31/08/2021"]
filtered_df=df[df["regionname"]=="SOUTH EAST"]
filtered_df=filtered_df[filtered_df["CDI"]<=4]
sns.set_style("darkgrid")
ax=sns.countplot(x="CDI",hue="lganame",palette=sns.color_palette("magma",2),linestyle = "-.",linewidth = .5,edgecolor = "white",data=filtered_df)
plt.sca(ax)
plt.xlabel("CDI",fontweight='bold')
plt.ylabel("Count of Postcode Area",fontweight='bold')
plt.title("Distribution of CDI in SOUTH EAST Region",fontsize=12, fontweight='bold')
ax.set_xticklabels(("CDI=2 Intensifying","CDI=4 Recovery"))
for container in ax.containers:
    ax.bar_label(container)
plt.legend(title="LGA",loc='upper left',prop={'size': 8})
plt.tight_layout()
plt.savefig("CDI_South_East.png",dpi=1100)
