import plotly.express as ck
import csv 
with open ("Student.csv")as file:
    data=csv.DictReader(file)
    fig=ck.scatter(data,x="Marks In Percentage",y="Days Present" )
    fig.show() 