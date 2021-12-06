import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
from pyecharts.charts import Pie
from pyecharts import options as opts
from pyecharts.globals import RenderType
from pyecharts.globals import ThemeType

names=sys.argv[1:4]

for region_name in names:
    if region_name =="South East":
        df=pd.read_csv("South Coast CDI.csv")
    else:
        df=pd.read_excel("Concatenated_data.xlsx")
    df["Date"]=pd.to_datetime(df["Date"])
    df=df[(df["Date"]=="30/09/2018") | (df["Date"]=="30/09/2019") | (df["Date"]=="30/09/2020") | (df["Date"]=="31/08/2021")]
    df=df[df["regionname"] == region_name.upper()]
    total=df["CDI"].count()
    non_drougnt=df.loc[df.CDI == 4,'CDI'].count() + df.loc[df.CDI == 5, 'CDI'].count()
    drought_affected=total-non_drougnt
    chart_data = [("Non Drought Areas",int(non_drougnt)),("Drought Affected Area",int(drought_affected))]
    pie = Pie()

    pie = Pie(opts.InitOpts(
        width="650px",
        height="450px",
        page_title=region_name,
        renderer= "svg",
        theme= "roma"))
        #for 


    pie.add(
        series_name="",
        data_pair=chart_data,
        radius=["30%","60%"],
        label_opts=opts.LabelOpts(formatter="{d}%", position="inside",font_size = 19,font_weight ="bold"
        ))

    pie.set_global_opts(
        title_opts=opts.TitleOpts(title=region_name,
        pos_left="7%"
        ))

    #pie.render(f"/Users/ruby/Desktop/{region_name}_Pie_Chart.html")     
  
    #Dear Blair, please change the above local path to yours to generate the chart😊)
