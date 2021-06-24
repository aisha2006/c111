import statistics as st
import pandas as pd
import plotly.figure_factory as ff
import random
import plotly.graph_objects as go
import csv

df = pd.read_csv("School2.csv")
score = df["Math_score"].tolist()

def random_set_of_mean(counter):
    scoreList = []
    for i in range(0,counter):
        randomIndexNumber = random.randint(0,len(score)-1)
        value = score[randomIndexNumber]
        scoreList.append(value)
    mean = st.mean(scoreList)
    return mean

meanList = []
for i in range(0,1000):
    set_of_means = random_set_of_mean(100)
    meanList.append(set_of_means)

mean = st.mean(meanList)
stdev = st.stdev(meanList)

first_stdev_start, first_stdev_end = mean-stdev,mean+stdev
second_stdev_start, second_stdev_end = mean-(2*stdev),mean+(2*stdev)
third_stdev_start, third_stdev_end = mean-(3*stdev),mean+(3*stdev)

df = pd.read_csv("School_1_Sample.csv")
score_sample_1 = df["Math_score"].tolist()
mean_sample_1 = st.mean(score_sample_1)
print(mean_sample_1)


fig_sample_1 = ff.create_distplot(
    [meanList],["MARKS"], show_hist=False
)
fig_sample_1.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines", name="MEAN"))
fig_sample_1.add_trace(go.Scatter(x=[mean_sample_1,mean_sample_1],y=[0,0.17],mode="lines", name="MEAN OF SAMPLE1"))
fig_sample_1.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,0.17],mode="lines", name="stdev 1 END"))
fig_sample_1.add_trace(go.Scatter(x=[second_stdev_end,second_stdev_end],y=[0,0.17],mode="lines", name="stdev 2 END"))
fig_sample_1.add_trace(go.Scatter(x=[third_stdev_end,third_stdev_end],y=[0,0.17],mode="lines", name="stdev 3 END"))
#fig_sample_1.show()


df = pd.read_csv("School_2_Sample.csv")
score_sample_2 = df["Math_score"].tolist()
mean_sample_2 = st.mean(score_sample_2)
print(mean_sample_2)

fig_sample_2 = ff.create_distplot(
    [meanList],["MARKS"], show_hist=False
)
fig_sample_2.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines", name="MEAN"))
fig_sample_2.add_trace(go.Scatter(x=[mean_sample_2,mean_sample_2],y=[0,0.17],mode="lines", name="MEAN OF SAMPLE2"))
fig_sample_2.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,0.17],mode="lines", name="stdev 1 END"))
fig_sample_2.add_trace(go.Scatter(x=[second_stdev_end,second_stdev_end],y=[0,0.17],mode="lines", name="stdev 2 END"))
fig_sample_2.add_trace(go.Scatter(x=[third_stdev_end,third_stdev_end],y=[0,0.17],mode="lines", name="stdev 3 END"))
#fig_sample_2.show()

df = pd.read_csv("School_3_Sample.csv")
score_sample_3 = df["Math_score"].tolist()
mean_sample_3 = st.mean(score_sample_3)
print(mean_sample_3)


fig_sample_3 = ff.create_distplot(
    [meanList],["MARKS"], show_hist=False
)
fig_sample_3.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines", name="MEAN"))
fig_sample_3.add_trace(go.Scatter(x=[mean_sample_3,mean_sample_3],y=[0,0.17],mode="lines", name="MEAN OF SAMPLE3"))
fig_sample_3.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,0.17],mode="lines", name="stdev 1 END"))
fig_sample_3.add_trace(go.Scatter(x=[second_stdev_end,second_stdev_end],y=[0,0.17],mode="lines", name="stdev 2 END"))
fig_sample_3.add_trace(go.Scatter(x=[third_stdev_end,third_stdev_end],y=[0,0.17],mode="lines", name="stdev 3 END"))
#fig_sample_3.show()

z_score =( mean - mean_sample_1)/stdev
print(z_score)
