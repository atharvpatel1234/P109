import plotly.figure_factory as ff 
import random
import statistics
import plotly.graph_objects as go
import pandas as pd 
df=pd.read_csv("Data.csv")
gender_list=df["gender"].to_list()
data=[]
for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    data.append(dice1+dice2)

mean=statistics.mean(data)
median=statistics.median(data)
mode=statistics.mode(data)
standarddeviation=statistics.stdev(data)
print(f"mean is {mean}")
print(f"median is {median}")
print(f"mode is {mode}")
print(f"standarddeviation is {standarddeviation}")

first_std_dev_start,first_std_dev_end=mean-standarddeviation,mean+standarddeviation
second_std_dev_start,second_std_dev_end=mean-(2*standarddeviation),mean+(2*standarddeviation)
third_std_dev_start,third_std_dev_end=mean-(3*standarddeviation),mean+(3*standarddeviation)

fig=ff.create_distplot([data],["Percentage"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[first_std_dev_start,first_std_dev_start],y=[0,0.17],mode="lines",name="standarddeviation1start"))
fig.add_trace(go.Scatter(x=[first_std_dev_end,first_std_dev_end],y=[0,0.17],mode="lines",name="standarddeviation1end"))
fig.add_trace(go.Scatter(x=[second_std_dev_start,second_std_dev_start],y=[0,0.17],mode="lines",name="standarddeviation2start"))
fig.add_trace(go.Scatter(x=[second_std_dev_end,second_std_dev_end],y=[0,0.17],mode="lines",name="standarddeviation2end"))
fig.add_trace(go.Scatter(x=[third_std_dev_start,third_std_dev_start],y=[0,0.17],mode="lines",name="standarddeviation3start"))
fig.add_trace(go.Scatter(x=[third_std_dev_end,third_std_dev_end],y=[0,0.17],mode="lines",name="standarddeviation3end"))


fig.show()

datawithinstd1=[result for result in data if result > first_std_dev_start and result < first_std_dev_end]
datawithinstd2=[result for result in data if result > second_std_dev_start and result < second_std_dev_end]
datawithinstd3=[result for result in data if result > third_std_dev_start and result < third_std_dev_end]

print("{}% of data lies within 1standarddeviation".format(len(datawithinstd1)*100.0/len(data)))
print("{}% of data lies within 2standarddeviation".format(len(datawithinstd2)*100.0/len(data)))
print("{}% of data lies within 3standarddeviation".format(len(datawithinstd3)*100.0/len(data)))