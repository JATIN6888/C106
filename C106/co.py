import plotly.express as py
import csv 
with open ("coffee.csv")as file:
    data=csv.DictReader(file)
    fig=py.scatter(data,x="Coffee in ml",y="sleep in hours" )
    fig.show() 