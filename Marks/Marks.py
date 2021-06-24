import statistics as st
import pandas as pd
import plotly.figure_factory as ff
import random
import plotly.graph_objects as go
import csv

df = pd.read_csv("studentMarks.csv")
score = df["Math_score"].tolist()
fig = ff.create_distplot(
    [score],["score"], show_hist = False
)
# fig.show()

#mean = st.mean(score)
# median = st.median(score)
# mode = st.mode(score)
# print(mean,median,mode)

stdev = st.stdev(score)
# print(stdev)

#Taking 1000 samples of 100 data points each
def random_set_of_mean(counter):
    scoreList = []
    for i in range(0,counter):
        randomIndexNumber = random.randint(0,len(score)-1)
        value = score[randomIndexNumber]
        scoreList.append(value)
    mean = st.mean(scoreList)
    return mean

#Number of samples = 1000
meanList = []
for i in range(0,1000):
    set_of_means = random_set_of_mean(100)
    meanList.append(set_of_means)

#mean & stdev of the sampling distribution
mean = st.mean(meanList)
stdev = st.stdev(meanList)
# print(mean,stdev)

first_stdev_start, first_stdev_end = mean-stdev,mean+stdev
second_stdev_start, second_stdev_end = mean-(2*stdev),mean+(2*stdev)
third_stdev_start, third_stdev_end = mean-(3*stdev),mean+(3*stdev)


fig = ff.create_distplot(
    [meanList],["marks"],show_hist=False
)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode = "lines", name="mean"))
fig.add_trace(go.Scatter(x=[first_stdev_start,first_stdev_start],y=[0,0.17],mode="lines", name="stdev 1 START"))
fig.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,0.17],mode="lines", name="stdev 1 END"))
fig.add_trace(go.Scatter(x=[second_stdev_start,second_stdev_start],y=[0,0.17],mode="lines", name="stdev 2 START"))
fig.add_trace(go.Scatter(x=[second_stdev_end,second_stdev_end],y=[0,0.17],mode="lines", name="stdev 2 END"))
fig.add_trace(go.Scatter(x=[third_stdev_start,third_stdev_start],y=[0,0.17],mode="lines", name="stdev 3 START"))
fig.add_trace(go.Scatter(x=[third_stdev_end,third_stdev_end],y=[0,0.17],mode="lines", name="stdev 3 END"))
# fig.show()

# #FIRST DATA OF INTERVENTION (ipad tablets)
# df = pd.read_csv("data1.csv")
# score_sample_1 = df["Math_score"].tolist()
# mean_sample_1 = st.mean(score)
# stdev_sample_1 = st.stdev(score)
# # print(mean_sample_1,stdev_sample_1)

# # print(first_stdev_start,first_stdev_end)
# # print(second_stdev_start,second_stdev_end)
# # print(third_stdev_start,third_stdev_end)

# fig_sample_1 = ff.create_distplot(
#     [score_sample_1],["first score of intervention"], show_hist=False
# )
# fig_sample_1.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines", name="MEAN"))
# fig_sample_1.add_trace(go.Scatter(x=[mean_sample_1,mean_sample_1],y=[0,0.17],mode="lines", name="stdev 1 START"))
# fig_sample_1.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,0.17],mode="lines", name="stdev 1 END"))
# fig_sample_1.add_trace(go.Scatter(x=[second_stdev_start,second_stdev_start],y=[0,0.17],mode="lines", name="stdev 2 START"))
# fig_sample_1.add_trace(go.Scatter(x=[second_stdev_end,second_stdev_end],y=[0,0.17],mode="lines", name="stdev 2 END"))
# fig_sample_1.add_trace(go.Scatter(x=[third_stdev_start,third_stdev_start],y=[0,0.17],mode="lines", name="stdev 3 START"))
# fig_sample_1.add_trace(go.Scatter(x=[third_stdev_end,third_stdev_end],y=[0,0.17],mode="lines", name="stdev 3 END"))
# fig_sample_1.show()

# #SECOND DATA OF INTERVENTION (extra classes)
# df = pd.read_csv("data3.csv")
# score_sample_1 = df["Math_score"].tolist()
# mean_sample_1 = st.mean(score)
# stdev_sample_1 = st.stdev(score)
# # print(mean_sample_1,stdev_sample_1)

# # print(first_stdev_start,first_stdev_end)
# # print(second_stdev_start,second_stdev_end)
# # print(third_stdev_start,third_stdev_end)

# fig_sample_1 = ff.create_distplot(
#     [score_sample_1],["first score of intervention"], show_hist=False
# )
# fig_sample_1.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines", name="MEAN"))
# fig_sample_1.add_trace(go.Scatter(x=[mean_sample_1,mean_sample_1],y=[0,0.17],mode="lines", name="MEAN OF INTERVENTION"))
# fig_sample_1.add_trace(go.Scatter(x=[first_stdev_start,first_stdev_start],y=[0,0.17],mode="lines", name="stdev 1 START"))
# fig_sample_1.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,0.17],mode="lines", name="stdev 1 END"))
# fig_sample_1.add_trace(go.Scatter(x=[second_stdev_start,second_stdev_start],y=[0,0.17],mode="lines", name="stdev 2 START"))
# fig_sample_1.add_trace(go.Scatter(x=[second_stdev_end,second_stdev_end],y=[0,0.17],mode="lines", name="stdev 2 END"))
# fig_sample_1.add_trace(go.Scatter(x=[third_stdev_start,third_stdev_start],y=[0,0.17],mode="lines", name="stdev 3 START"))
# fig_sample_1.add_trace(go.Scatter(x=[third_stdev_end,third_stdev_end],y=[0,0.17],mode="lines", name="stdev 3 END"))
# fig_sample_1.show()

#THIRD DATA OF INTERVENTION (assignments)
df = pd.read_csv("data3.csv")
score_sample_1 = df["Math_score"].tolist()
mean_sample_1 = st.mean(score)
stdev_sample_1 = st.stdev(score)
# print(mean_sample_1,stdev_sample_1)

# print(first_stdev_start,first_stdev_end)
# print(second_stdev_start,second_stdev_end)
# print(third_stdev_start,third_stdev_end)

fig_sample_1 = ff.create_distplot(
    [score_sample_1],["first score of intervention"], show_hist=False
)
fig_sample_1.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines", name="MEAN"))
fig_sample_1.add_trace(go.Scatter(x=[mean_sample_1,mean_sample_1],y=[0,0.17],mode="lines", name="MEAN OF INTERVENTION"))
fig_sample_1.add_trace(go.Scatter(x=[first_stdev_start,first_stdev_start],y=[0,0.17],mode="lines", name="stdev 1 START"))
fig_sample_1.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,0.17],mode="lines", name="stdev 1 END"))
fig_sample_1.add_trace(go.Scatter(x=[second_stdev_start,second_stdev_start],y=[0,0.17],mode="lines", name="stdev 2 START"))
fig_sample_1.add_trace(go.Scatter(x=[second_stdev_end,second_stdev_end],y=[0,0.17],mode="lines", name="stdev 2 END"))
fig_sample_1.add_trace(go.Scatter(x=[third_stdev_start,third_stdev_start],y=[0,0.17],mode="lines", name="stdev 3 START"))
fig_sample_1.add_trace(go.Scatter(x=[third_stdev_end,third_stdev_end],y=[0,0.17],mode="lines", name="stdev 3 END"))
fig_sample_1.show()

