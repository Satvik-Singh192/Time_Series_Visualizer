import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

month={'1':'January','2':'Feburary','3':'March','4':"April",'5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'Novermber','12':'December'}

df=pd.read_csv('C:/Users/SHALINI SINGH/Desktop/VS Code_Program/Page_View_Time_Visualizer/fcc-forum-pageviews.csv',index_col=0,names=['Views'])
df_sorted=df.sort_values("Views")
con=len(df)
ind=round(0.20*con)
df_prime=df_sorted.iloc[0:ind,:]
sum=0
c=0
x=1
def draw_line_plot():
    plt.plot(df_prime.index,df_prime["Views"],color='red')
    plt.xlabel="Date"
    plt.ylabel="Page Views"
    plt.title="Daily FreeCodeCamp Forum Page"
    plt.show()
  
m=[]
def draw_bar_plot():
    avg_per_month=[]
    for i in range(1,13):
        sum=0
        c=0
        for j in df.index:
            r=j[6]
            if r==str(i):
                sum+=df.loc[j,"Views"]
                c+=1
                if month[r] not in m:
                    m.append(month[r])
            else:
                continue
        if c!=0:    
            avg_per_month.append(round(sum/c))
    plt.bar(m,avg_per_month)
    plt.xlabel("Month")
    plt.ylabel("Average Views per month")
    plt.title("Freecodecamp's Data")
    plt.show()

def draw_box_plot():
    plt.subplot(1,2,1)
    qtr={"Qtr1":0,"Qtr2":0,'Qtr3':0,'Qtr4':0}
    plt.title("Quaterly box plot")
    plt.xlabel("Quarters")
    plt.ylabel("Views")
    for i in df.index:
        r=i[5:7]
        if (r) in ['01','02','03']:
            qtr["Qtr1"]+=df.loc[i,"Views"]
        elif (r) in ['04','05','06']:
            qtr['Qtr2']+=df.loc[i,"Views"]
        elif (r) in ['07','08','09']:
            qtr['Qtr3']+=df.loc[i,"Views"]
        elif (r) in ['10','11','12']:
            qtr['Qtr4']+=df.loc[i,"Views"]
        x=list(qtr.keys())
        y=list(qtr.values())
    plt.boxplot(y)
    plt.show()
    
    plt.subplot(1,2,2)
    plt.title("Monthly box plot")
    d={'01':0,'02':0,'03':0,'04':0,'05':0,'06':0,'07':0,'08':0,'09':0,'10':0,'11':0,'12':0}
    for i in df.index:
        r=i[5:7]
        d[r]+=df.loc[i,"Views"]
    plt.boxplot(list(d.values()))
    plt.show()
        
