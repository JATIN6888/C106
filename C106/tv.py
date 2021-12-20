import plotly.express as pk
import csv 
with open ("tv.csv")as file:
    data=csv.DictReader(file)
    fig=pk.scatter(data,x="Size of TV",y="	Average time spent watching TV in a week (hours)" )
    fig.show() 