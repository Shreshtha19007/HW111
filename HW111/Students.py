import plotly.figure_factory as ff
import pandas as pd
import csv
import random
import statistics
import plotly.graph_objects as go

df=pd.read_csv("data.csv")
data=df["claps"].tolist()

def random_set_of_mean(counter):
    dataset=[]
    for i in range (0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

mean_list=[]
for i in range(0,1000):
    set_of_means=random_set_of_mean(100)
    mean_list.append(set_of_means)

stdev=statistics.stdev(mean_list)
mean=statistics.mean(mean_list)
print(mean)

startstdev,endstdev=mean-stdev,mean+stdev
secondstartstdev,secondendstdev=mean-(2*stdev),mean+(2*stdev)
thirdstartstdev,thirdendstdev=mean-(3*stdev),mean+(3*stdev)

print(startstdev,endstdev)
print(secondstartstdev,secondendstdev)
print(thirdstartstdev,thirdendstdev)

figure=ff.create_distplot(
    [mean_list],
["Claps"],
show_hist=False
)
figure.add_trace(go.Scatter(
    x=[mean,mean],
    y=[0,0.17],
    mode="lines",
    name="MEAN"
))
figure.add_trace(go.Scatter(
    x=[startstdev,startstdev],
    y=[0,0.17],
    mode="lines",
    name="startstdev"
))
figure.add_trace(go.Scatter(
    x=[secondstartstdev,secondstartstdev],
    y=[0,0.17],
    mode="lines",
    name="secondstartstdev"
))
figure.add_trace(go.Scatter(
    x=[thirdstartstdev,thirdstartstdev],
    y=[0,0.17],
    mode="lines",
    name="thirdstartstdev"
))


figure.show()
