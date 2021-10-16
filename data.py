import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import statistics
import random

df = pd.read_csv("data.csv")
data = df["reading_time"].tolist()
population_mean = statistics.mean(data)
print("The mean of the population is: " + str(mean))
population_stdDev = statistics.stdev(data)
print("The standard deviation of the population is: " + str(population_stdDev))

def rand_set_mean(counter):
    dataset=[]
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return(mean)

def show_fig(mean_list):
    df= mean_list
    mean= statistics.mean(mean_list)
    stdDev = statistics.stdev(mean_list)
    fig = ff.create_distplot([df], ["reading_time"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0,1], mode='lines', name="Mean"))
    print("Mean is: " + str(mean))
    print("Standard deviation is: " + str(stdDev))
    fig.show()

def setup():
    list_mean=[]
    for i in range(0,1000):
        setMeans=random_set_of_mean(100)
        list_mean.append(setMeans)
    show_fig(list_mean)

setup()