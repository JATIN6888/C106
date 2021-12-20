import plotly.express as px
import csv 
with open ("ice.csv")as file:
    data=csv.DictReader(file)
    fig=px.scatter(data,x="Temperature",y="Ice-cream Sales" )
    fig.show()